encoded_password = b"zqttoped"

for _ in range(4):
    encoded_password = encoded_password.hex()
    encoded_password = encoded_password.encode("utf-8")
print(encoded_password)
