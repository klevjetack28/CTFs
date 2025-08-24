from pwn import *

flag = ""

p = process("/challenge/run")

message = p.read().decode();
print(message)

def get_key(message):
	key = message.split("Key (b64): ")[1].split("\nFlag")[0]
	key = base64.b64decode(key)
	return key

def get_flag_string(message):
	flag_string = message.split("Ciphertext (b64): ")[1].split("\n")[0]
	flag_string = base64.b64decode(flag_string)
	return flag_string

key = get_key(message)
flag_string = get_flag_string(message)
IV = flag_string[:16]
flag_string = flag_string[16:]

print(key)
print(IV)
print(flag_string)

from Crypto.Cipher import AES

def decrypt_aes_cbc(ciphertext, key, iv):
    """Decrypts AES CBC encrypted data."""

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    # Remove padding (if applicable)
    unpad = lambda s: s[:-ord(s[len(s)-1:])] 
    plaintext = unpad(plaintext)

    return plaintext

print(decrypt_aes_cbc(flag_string, key, IV))
