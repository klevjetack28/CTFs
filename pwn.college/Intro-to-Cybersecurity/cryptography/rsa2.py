from pwn import *
import base64

# GPT Generated code for the mod_inverse
def extended_gcd(a, b):
    """Returns the greatest common divisor of a and b, and the coefficients x, y 
    such that a * x + b * y = gcd(a, b)"""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(e, phi_n):
    """Returns the modular inverse of e modulo phi_n using the extended Euclidean algorithm."""
    gcd, x, y = extended_gcd(e, phi_n)
    if gcd != 1:
        raise ValueError(f"Inverse does not exist for e = {e} and phi_n = {phi_n}")
    else:
        return x % phi_n

p = process("/challenge/run")
message1 = p.recvuntil(b"q = ").decode()
message2 = p.read().decode()
print(message1)
print(message2)

e = message1.split("\n")[0].split()[2]
print(f"E: {e}")
p = message1.split("\n")[1].split()[2]
print(f"P: {p}")
q = message2.split("\n")[0].split()[0]
print(f"Q: {q}")

n = int(p, 16) * int(q, 16)

d = mod_inverse(int(e, 16), (int(p, 16) - 1) * (int(q, 16) - 1))

flag = message2.split("\n")[1].split()[3]
flag = base64.b64decode(flag)
flag = pow(int.from_bytes(flag, "little"), d, n).to_bytes(256, "little")
print(f"Flag: {flag}")
