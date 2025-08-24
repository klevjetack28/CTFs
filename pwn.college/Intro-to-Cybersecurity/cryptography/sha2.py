from pwn import *
import base64
import hashlib

p = process("/challenge/run")

challenge_data = base64.b64decode(p.read().decode().split()[59])
print(challenge_data)

attack_key = "0000"
i = 0
for i in range(0x11111111111111111111111111111111):
        hash = hashlib.sha256(challenge_data + i.to_bytes(256, "little")).hexdigest()
        if i % 1000000 == 0:
                print(hash)
        if hash[:4] == attack_key:
                print(i)
                print(hash)
                break

#p.write(base64.b64encode(i.to_bytes(256, "little") + challenge_data) + "\n".encode())
p.write(base64.b64encode(i.to_bytes(256, "little")) + "\n".encode())
print(p.read())
p.close()


