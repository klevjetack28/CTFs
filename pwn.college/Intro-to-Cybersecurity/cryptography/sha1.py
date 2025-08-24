from pwn import *
import base64
import hashlib

attack_key = "125a82"
hash = None
i = 0
for i in range(0x11111111111111111111111111111111):
	hash = hashlib.sha256(i.to_bytes(256, "little")).hexdigest()
	if i % 1000000 == 0:
		print(hash)
	if hash[:6] == attack_key:
		print(i)
		print(hash)
		break

p = process("/challenge/run")
print(p.read())
p.write(base64.b64encode(i.to_bytes(256, "little")) + "\n".encode())
print(p.read())
p.close()
