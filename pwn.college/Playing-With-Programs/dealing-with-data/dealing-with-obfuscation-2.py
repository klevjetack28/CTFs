import base64
correct_password = b"\xc8\xf2#\xb4\x94@\x82N"

correct_password = correct_password[::-1]
correct_password = correct_password.hex().encode("l1")
correct_password = correct_password[::-1]
correct_password = correct_password[::-1]

correct_password = correct_password[::-1]
correct_password = bytes.fromhex(correct_password.decode("l1"))
correct_password = base64.b64decode(correct_password.decode("l1"))
correct_password = correct_password[::-1]

print(correct_password)
