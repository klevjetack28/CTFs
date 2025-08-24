from pwn import *
import base64
from Crypto.Util.Padding import pad
from Crypto.Util import strxor
flag = ""

p = process(["/challenge/dispatcher", "flag"])

message = p.read().decode()[:-1]
#print(f"Message: {message}")

def break_into_chunks(ciphertext, chunk_size=16):
    chunks = [ciphertext[i:i+chunk_size] for i in range(0, len(ciphertext), chunk_size)]
    return chunks

ciphertext = base64.b64decode(message.split()[1])
chunks = break_into_chunks(ciphertext)
print(f"Ciphertext: {ciphertext}")
print(f"Chunks: {chunks}")

def attack(newChunk, currChunk, prevChunk):
	decrypted = bytearray(16)
	plaintext = bytearray(16)

	for i in range(15, -1, -1):
		for value in range(256):
			newChunk[i] = value
			print(f"New Chunk: {newChunk}")
			newCiphertext = newChunk + currChunk

			newCiphertext = base64.b64encode(newCiphertext)
#			print(newCiphertext)

			message = "TASK: " + newCiphertext.decode() + "\n"
#			print(message)

			worker = process(["/challenge/worker", message])
			worker.sendline(message)
			worker_output = worker.recvline()
#			print(f"Worker Output: {worker_output.decode().strip()}")

			if worker_output != "Traceback (most recent call last):\n".encode():
				worker.close()
				decrypted[i] = newChunk[i] ^ (16 - i)
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

	return plaintext

flag = ""
for i in range(len(chunks) - 1, 0, -1):
	print(chunks)
	print(f"Current Chunk: {chunks[i]}")
	print(f"Previous Chunk: {chunks[i - 1]}")
	newIV = bytearray(16)
	flag = attack(newIV, chunks[i], chunks[i - 1]).decode() + flag

print(flag)


