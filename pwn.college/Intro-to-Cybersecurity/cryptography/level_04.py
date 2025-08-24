
while True:
	a = input("Enter string 1: ")
	b = input("Enter string 2: ")

	a_byte = a.encode(encoding="utf-8")
	b_byte = b.encode(encoding="utf-8")

	c = bytes(a ^ b for a, b in zip(a_byte, b_byte))
	print(c.decode())
