import hashlib

result = hashlib.sha256(b"GOUGH").hexdigest()

count = 0
for value in result:
    print(str(count) + ": " + value)
    count += 1
