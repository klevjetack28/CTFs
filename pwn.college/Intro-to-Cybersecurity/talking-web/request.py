import requests
#Make an HTTP request to 127.0.0.1 on port 80 to get the flag.
#The HTTP request must specify a content type HTTP header of 'application/json'
#Must send an HTTP POST with the body as a JSON object that has:
#	a pair with name of `a` and a value of 416b66726423db0a07a7682302f3b59c
#	a pair with name of `b` and a value of a object that has:
#		a pair with name of `c` and a value of b4f0257c
#		a pair with name of `d` and a value that is a list with the following elements:
#			6bf43243
#			47d2e84f 770548eb&04a65b35#35cc5f2e

#headers = {
#	"Content-Length": "34", 
#	"Content-Type": "application/x-www-form-urlencoded"
#}
#payload = {
#	"a": "416b66726423db0a07a7682302f3b59c",
#	"b": {
#		"c": "b4f0257c",
#		"d": ["6bf43243", "47d2e84f 770548eb&04a65b35#35cc5f2e"]
#	}
#}

r = requests.post("http://127.0.0.1:80")

print(r.text)
