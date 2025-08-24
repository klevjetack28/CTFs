import base64

#One-Time Pad Key (b64): HHmgomHgM3sHWxvIGUFeeQaakOiB1u7sxl4JgJBv+CbZvKeG8K7MzT8oCCkqUcAYwUE5Izv4EJkFAA==
#Flag Ciphertext (b64): bA7OjAKPXxdiPH6zIXA1L0DFw6vZkK+Ktyxh6vE8l1a99JDFt/G941t6cmdQHIRUtghtbguhas54Cg==

a = input("Enter OTP: ")
b = input("Enter cipertext: ")

a_decode = base64.b64decode(a)
b_decode = base64.b64decode(b)

c = bytes(a ^ b for a, b in zip(a_decode, b_decode))
print(c.decode())

