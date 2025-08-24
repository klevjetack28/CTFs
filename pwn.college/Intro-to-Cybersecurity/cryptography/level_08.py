import base64
from Crypto.Cipher import AES

a = input("Enter AES key: ")
b = input("Enter ciphertext: ")

a_decode = base64.b64decode(a)
b_decode = base64.b64decode(b)

cipher = AES.new(key=a_decode, mode=AES.MODE_ECB)
print(cipher.decrypt(b_decode))
