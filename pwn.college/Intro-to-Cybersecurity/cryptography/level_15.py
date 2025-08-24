import requests
import base64

flag = ""
attack_string = "00000000000000|"
codebook = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSYTUVWXYZ0123456789-_.{}"
pad_length = 62

def gen_message(c):
	return attack_string + c + "0" * pad_length

def reset():
	requests.post("http://challenge.localhost:80/reset")

def send_message(message):
	DATA = {"content": message}
	r = requests.post("http://challenge.localhost:80", data = DATA)

	return r.text

def parse_response(response):
        return response.split("<pre>")[1].split("</pre>")[0]

def split_sections(data):
        decoded_data = base64.b64decode(data)

        chunk_size = 16
        chunks = [decoded_data[i:i + chunk_size] for i in range(0, len(decoded_data), chunk_size)]

        base64_chunks = [base64.b64encode(chunk).decode('utf-8') for chunk in chunks]
        return base64_chunks

while len(flag) <= 57:
	for c in codebook:
		reset()
		message = send_message(gen_message(c))
		parsed = parse_response(message)
		split = split_sections(parsed)
		if split[0] == split[4]:
			flag += c
			attack_string = attack_string[1:] + c
			pad_length -= 1
			print(flag)
			break;

print("------------------------------------------------------\n\n")
print(flag)
print("\n\n------------------------------------------------------")
