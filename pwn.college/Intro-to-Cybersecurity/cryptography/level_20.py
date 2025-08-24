from pwn import *
import base64
from Crypto.Util.Padding import pad
from Crypto.Util import strxor
flag = ""

p = process(["/challenge/dispatcher"])

message = p.read().decode()[:-1]
#print(f"Message: {message}")

def break_into_chunks(ciphertext, block_size=16):
    chunks = []

    for i in range(0, len(ciphertext), block_size):
        chunk = ciphertext[i:i+block_size]

        if len(chunk) < block_size:
            padding_length = block_size - len(chunk)
            chunk = chunk + bytes([padding_length] * padding_length)
        chunks.append(chunk)

    return chunks


attack_message = b"please give me the flag, kind worker process!"
attack_chunks = break_into_chunks(attack_message)
print(attack_chunks)

ciphertext = base64.b64decode(message.split()[1])
chunks = break_into_chunks(ciphertext)
print(f"Ciphertext: {ciphertext}")
print(f"Chunks: {chunks}")

def attack(newChunk, currChunk, prevChunk, newPlaintext):
	decrypted = bytearray(16)
	plaintext = bytearray(16)
	modifyChunk = bytearray(16)
	modifyChunkPlaintext = bytearray(16)

	for i in range(15, -1, -1):
		for value in range(256):
			newChunk[i] = value
			print(f"New Chunk: {newChunk}")
			newCiphertext = newChunk + currChunk

			newCiphertext = base64.b64encode(newCiphertext)
#			print(newCiphertext)

			message = "TASK: " + newCiphertext.decode() + "\n"
#			print(message)

			worker = process(["/challenge/worker"])
			worker.sendline(message)
			worker_output = worker.recvline()
#			print(f"Worker Output: {worker_output.decode().strip()}")

			if worker_output != "Traceback (most recent call last):\n".encode():
				worker.close()
				decrypted[i] = newChunk[i] ^ (16 - i)
				modifyChunk[i] = newPlaintext[i] ^ decrypted[i]
				print(f"Modify Chunk: {modifyChunk}")
				modifyChunkPlaintext[i] = decrypted[i] ^ modifyChunk[i]
				print(f"Modify Chunk Plaintext: {modifyChunkPlaintext}")
				plaintext[i] = decrypted[i] ^ prevChunk[i]
				print(f"Plaintext: {plaintext}")
				for k in range(15 - i, -1, -1):
					print(f"K: {k}")
					print(f"Pad: {16 - i}")
					print(f"Decrypted: {decrypted}")
					newChunk[15 - k] = decrypted[15 - k] ^ (17 - i)
					print(f"Update Chunk: {newChunk}")

				break

			worker.close()

	print(f"Return Value: {modifyChunk}")
	return modifyChunk

modifiedCiphertext = b""
for c in chunks:
	modifiedCiphertext += c
print(modifiedCiphertext)
modifiedCiphertext = b""

for i in range(len(attack_chunks) - 1, -1, -1):
	print(f"Attack Chunk: {attack_chunks[i]}")
	print(f"Current Chunk: {chunks[1]}")
	print(f"Previous Chunk: {chunks[0]}")
	newIV = bytearray(16)
	print(f"I: {i}")
	print(f"Chunk[0]: {chunks[0]}")
	chunks[0] = attack(newIV, chunks[1], chunks[0], attack_chunks[i])
	chunks.insert(0, bytearray(16))
	print(f"Finalized Block: {chunks}")

chunks.pop(0)
print(f"Chunks After Pop: {chunks}")
for c in chunks:
	modifiedCiphertext += c
print(f"Modified Ciphertext Plain: {modifiedCiphertext}")

w = process(["/challenge/worker"])
modifiedCiphertext = base64.b64encode(modifiedCiphertext)
print(f"Modified Ciphertext Base64: {modifiedCiphertext}")
modifiedCiphertext = "TASK: " + modifiedCiphertext.decode() + "\n"
print(f"Modified Ciphertext Formatted {modifiedCiphertext}")
w.sendline(modifiedCiphertext)
print(w.recvline())
print(w.recvline())
print(w.recvline())
print(w.recvline())
w.close()
