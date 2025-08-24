lines = 0
post_requests = 0
get_requests = 0
unique_params = ["/*", "session", "xss", ";", "<script>", "javascript", "&&", "||", "admin", r"\.\./", "--", "WEB-INF/web.xml", "AND", "OR", "%"]
unique_requests = 0
response_code = 0
chunks = []
codes = {'404': 0, '400': 0, '200': 0, '301': 0, 'HTTP/1.1': 0, '303': 0, '500': 0, '403': 0, '302': 0}
uris = dict()
requested_resources = dict()

with open("log.txt", "r") as file:
    for line in file:
        lines += 1
        chunks = line.split("\"")
        response_code = chunks[3].split(" ")
        uri = chunks[4].split(" ")
        
        if uri[0] in uris:
            uris[uri[0]] += 1
        else:
            uris[uri[0]] = 1

        resource = chunks[2].split(" ")
        
        if len(resource) >= 2:
            if resource[1] in requested_resources:
                requested_resources[resource[1]] += 1
            else:
                requested_resources[resource[1]] = 1
        
        if len(response_code) >= 2:
            codes[response_code[1]] += 1
        
        if "POST" in chunks[2]:
            post_requests += 1
        elif "GET" in chunks[2]:
            get_requests += 1
        
        for unique in unique_params:
            if unique == "admin" and unique in chunks[2] and unique in chunks[4] and (len(response_code) < 4 or int(response_code[1]) < 400):
                unique_requests += 1
                break;
            elif unique in chunks[2] or unique in chunks[4]:
                unique_requests += 1 
                break;

        


print(f"Number of lines: {lines}")
print(f"Number of POST requests: {post_requests}")
print(f"Number of GET requests: {get_requests}")
print(f"Number of unique requests: {unique_requests}")
print(f"Dict of response codes: {codes}")

max = 0
max_uri = ""
for key, value in uris.items():
    if value >= max:
        max = value
        max_uri = key

print(f"Most used uri: {max_uri}")

max = 0
max_request = ""
for key, value in requested_resources.items():
    if value >= max:
        max = value
        max_request = key

print(f"Most requested resource: {max_request}")
