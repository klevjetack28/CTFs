from pwn import *
import base64

global prepend_string

flag = "000000000000000000000000000000000000000000000000000000000"
prepend = "000000000000000000000000000000000000000000000000000000000000000"
count = 0
codebook = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.-{}"
p = process("/challenge/run")

def encPlain(c):
	p.write(b'1\n')
	p.read()
	p.write((flag[-15:] + c).encode() + b'\n')
	return p.read()

def prependFlag():
	p.write(b'2\n')
	p.read()

	p.write(prepend.encode() + b'\n')

	return p.read()

def parse_response(response, enc, num_blocks):
	global pre_10
	if pre_10 < 9:
		response = response.split("Result: ")[1].split("\n")[0]
	else :
		response = response.split("Result: ")[1].split("\n\n")[0]
	decoded_data = base64.b64decode(response)

	chunk_size = 16
	chunks = [decoded_data[i:i + chunk_size] for i in range(0, len(decoded_data), chunk_size)]

	# Step 3: Re-encode each chunk back to Base64
	base64_chunks = [base64.b64encode(chunk).decode('utf-8') for chunk in chunks]
	return base64_chunks
p.read()

global pre_10
pre_10 = 1
while (count < 57):
	enc1 = prependFlag().decode()
	enc1 = parse_response(enc1, 1, 10)
	pre_10 += 1
	for c in codebook:
		enc2 = encPlain(c).decode()
		enc2 = parse_response(enc2, 2, 10)
		pre_10 += 1
		if enc1[3] == enc2[0]:
			flag = flag[1:] + c
			print(flag)
			prepend = prepend[1:]
			count += 1
			break;

p.close()

print("------------------------------------------------------\n\n")
print(flag)
print("\n\n------------------------------------------------------")

