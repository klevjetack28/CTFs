from pwn import *
import base64

p = process("/challenge/run")
print(p.read())
e = p.read().decode().split()[1]
message = p.read().decode().split()
d = message[1]
n = message[3]
challenge = message[5]

response = pow(int(challenge, 16), int(d, 16), int(n, 16))
p.write(hex(response) + "\n")
print(p.read())
p.close()
