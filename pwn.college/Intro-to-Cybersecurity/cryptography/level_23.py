from pwn import *
import base64

p = process("/challenge/run")
message1 = p.read().decode()
message2 = p.read().decode()
print(message1)
print(message2)

n = message1.split("\n")[0].split()[3]
print(f"N: {n}")
e = message1.split("\n")[1].split()[3]
print(f"E: {e}")
d = message2.split("\n")[0].split()[3]
print(f"D: {d}")
flag = message2.split("\n")[1].split()[3]
flag = base64.b64decode(flag)
flag = pow(int.from_bytes(flag, "little"), int(d, 16), int(n, 16)).to_bytes(256, "little")
print(f"Flag: {flag}")
