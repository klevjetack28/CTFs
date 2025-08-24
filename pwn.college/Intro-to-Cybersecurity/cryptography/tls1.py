from pwn import *
import base64
from hashlib import sha256
from Crypto.PublicKey import RSA
p = process("/challenge/run")

p.read()
keyd = p.read().split()[3]
message = p.read().split()
certificate = base64.b64decode(message[3])
cert_signature = base64.b64decode(message[8])

n = certificate.split()[6].decode().rstrip()
n = n[:-2]
root_n = n
key = RSA.generate(1024)
n = key.n

certificate = f'{{"name": "user", "key": {{"e": 65537, "n": {n}}}, "signer": "root"}}'
p.write(base64.b64encode(certificate.encode()) + "\n".encode())
p.read()
certificate = sha256(certificate.encode()).digest()
user_signature = pow(int.from_bytes(certificate, "little"), int(keyd, 16), int(root_n))
p.write(base64.b64encode(user_signature.to_bytes(256, "little")) + "\n".encode())
ciphertext = p.read().split()[3]
ciphertext = base64.b64decode(ciphertext)
print(ciphertext)
flag = pow(int.from_bytes(ciphertext, "little"), key.d, key.n)
print(flag.to_bytes(256, "little"))
