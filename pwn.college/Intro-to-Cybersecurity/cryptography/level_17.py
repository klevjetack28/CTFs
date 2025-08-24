from pwn import *
from Crypto.Util.Padding import pad

flag = ""

p = process("/challenge/dispatcher")

message = p.read().decode();
#print(message)
#print(len(message))

ciphertext = base64.b64decode(message.split()[1])
#print(ciphertext)
#print(len(ciphertext))

IV, ciphertext = ciphertext[:16], ciphertext[16:]
#print(IV)
#print(len(IV))
#print(ciphertext)
#print(len(ciphertext))

def xor_bytes(str1, str2):
    """XORs two byte strings."""
    return bytes([a ^ b for a, b in zip(str1, str2)])

# Example usage:
str1 = pad(b'sleep', 16)
str2 = pad(b'flag!', 16)
result = xor_bytes(str1, str2)
#print(result)

IV = xor_bytes(result, IV)

attack_cipher = IV + ciphertext
#print(attack_cipher)
#print(len(attack_cipher))

attack_string = "TASK: " + base64.b64encode(attack_cipher).decode()
print(attack_string)
#print(len(attack_string))
