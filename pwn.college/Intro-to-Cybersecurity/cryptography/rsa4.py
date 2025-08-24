from pwn import *
import base64
from Crypto.PublicKey import RSA
from Crypto.Util.number import getPrime

p = process("/challenge/run")

key = RSA.generate(1024)

p.read()
p.write(hex(key.e) + "\n")
p.read()
p.write(hex(key.n) + "\n")
challenge = int(p.read().split()[1], 16)
output = pow(challenge, key.d, key.n)
p.write(hex(output) + "\n")
ciphertext = base64.b64decode(p.read().split()[3])
print(ciphertext)
ciphertext = int.from_bytes(ciphertext, "little")
flag = pow(ciphertext, key.d, key.n)
print(flag.to_bytes(256, "little"))
p.close()
