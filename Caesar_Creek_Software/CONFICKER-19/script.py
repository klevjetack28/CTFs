from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util.Padding import unpad
import binascii

# Example AES parameters
key = b'Prestidigitation'  # 16 bytes for AES-128
ciphertext = "e1dbfd6826a14f279fafe76982333070"
ciphertext_2 = "a0595e10eec5ffd64cf3569eac102451"  

def decrypt_message(ciphertext_hex):
    ciphertext = binascii.unhexlify(ciphertext_hex)

    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_ECB)  # Change mode if needed

    # Decrypt
    decrypted_data = cipher.decrypt(ciphertext)

    # Print Decrypt
    print("Decrypted data (bytes):", decrypted_data)

    # Reverse the manipulation
    original_block = reverse_xor(decrypted_data)

    return original_block

def reverse_xor(data):
    block = bytearray(data)
    prev = 0
    for i in range(15):  # 0 to 13, for a total of 14 iterations
        block[15 - i] = block[15 - i] ^ block[14 - i]
    return block

decrypted_1 = decrypt_message(ciphertext)
decrypted_2 = decrypt_message(ciphertext_2)

print("Decrypted Message 1 (bytes):", decrypted_1)
print("Decrypted Message 1 (string):", decrypted_1.decode('utf-8', errors='ignore'))

print("Decrypted Message 2 (bytes):", decrypted_2)
print("Decrypted Message 2 (string):", decrypted_2.decode('utf-8', errors='ignore'))


