import base64

def break_into_chunks(ciphertext, chunk_size=16):
    chunks = [bytearray(ciphertext[i:i+chunk_size]) for i in range(0, len(ciphertext), chunk_size)]
    return chunks

def xor_bytearrays(ba1, ba2):
    return bytearray(a ^ b for a, b in zip(ba1, ba2))

cookie = input("Enter your cookie: ")

b64_decoded_cookie = base64.b64decode(cookie)

cookie_chunks = break_into_chunks(b64_decoded_cookie)

new_role = b'{"role":"admin"}'

cookie_chunks[1] = xor_bytearrays(cookie_chunks[1], new_role)
cookie_chunks[1] = xor_bytearrays(cookie_chunks[1], b',"role":"users"}')
print(cookie_chunks[1])

new_cookie = bytearray()
#for chunk in cookie_chunks:
#    new_cookie += chunk
new_cookie = cookie_chunks[1] + cookie_chunks[2] + cookie_chunks[3]
print(new_cookie)
new_encoded_cookie = base64.b64encode(new_cookie)

print(f"New Cookie: {new_encoded_cookie}")
