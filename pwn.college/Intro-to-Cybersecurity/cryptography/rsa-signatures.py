from pwn import *
import base64

flag_int = int.from_bytes(b'flag', byteorder='little')
print(f"Flag Int: {flag_int}")

def prime_factorize(num):
    factors = []
    # Check for factor of 2 first
    while num % 2 == 0:
        factors.append(2)
        num //= 2
    # Check for odd factors from 3 upwards
    factor = 3
    while factor * factor <= num:
        while num % factor == 0:
            factors.append(factor)
            num //= factor
        factor += 2
    # If num is still greater than 2, it's prime
    if num > 2:
        factors.append(num)

    return factors

factors = prime_factorize(flag_int)
signed_factors = []
for i in range(len(factors)):
	print(f"Prime{i}: {factors[i]}")
	param = base64.b64encode(factors[i].to_bytes(256, "little"))
	p = process(["/challenge/dispatcher", param])

	signed_factors.append(base64.b64decode(p.read().decode().split()[3]))
	print(signed_factors[i])

	p.close()

enc_flag = 1
for s_factor in signed_factors:
	enc_flag *= int.from_bytes(s_factor, byteorder='little')

enc_flag = base64.b64encode(enc_flag.to_bytes(2048, "little"))

p = process(["/challenge/worker", enc_flag])
print(p.read())
print(p.read())
p.close()
