from pwn import *
import base64

flag = ""
attack_string = "\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30"
codebook = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSYTUVWXYZ0123456789-_.{}"
pad_length = 63
p = process("/challenge/run")

def gen_message(c):
	message = ((attack_string + c).encode() + b"\x30" * pad_length)
	return message

def send_message(message):
	message = base64.b64encode(message)
	p.write(message + b"\n")
	sleep(0.02)
	return p.read()

def parse_response(response):
	return response.split(" ")[1].split("\n")[0]

def split_sections(data):
	decoded_data = base64.b64decode(data)

	chunk_size = 16
	chunks = [decoded_data[i:i + chunk_size] for i in range(0, len(decoded_data), chunk_size)]

	base64_chunks = [base64.b64encode(chunk).decode('utf-8') for chunk in chunks]
	return base64_chunks

p.read()
while len(flag) < 57:
	for c in codebook:
		message = gen_message(c)
		response = send_message(message).decode()
		data = parse_response(response)
		sections = split_sections(data)
		if sections[0] == sections[4]:
			flag += c
			attack_string = attack_string[1:] + c
			pad_length -= 1
			print(flag)
			break
p.close()

print("------------------------------------------------------\n\n")
print(flag)
print("\n\n------------------------------------------------------")
