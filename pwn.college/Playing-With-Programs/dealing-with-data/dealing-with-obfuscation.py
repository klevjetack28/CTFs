import base64
correct_password = b'_~"\x13\x13a\x90i'
correct_password = base64.b64encode(correct_password)
correct_password = correct_password[::-1]
correct_password = correct_password.hex().encode("l1")
correct_password = correct_password.hex().encode("l1")
print(correct_password)
