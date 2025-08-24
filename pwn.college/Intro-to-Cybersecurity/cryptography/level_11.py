from pwn import *

flag = ""
count = 0
codebook = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.-{}"

p = process("/challenge/run")

def encPlain(c):
	p.write(b'1\n')
	p.read()
	p.write(c.encode() + flag.encode() + b'\n')

	return p.read()

def encFlag():
	p.write(b'2\n')
	p.read()
	p.write(str(count + 1).encode() + b'\n')

	return p.read()

p.read()
while(count < 57):
	print(flag)
	enc1 = encFlag().decode()
	enc1 = enc1.split('Result: ')[1].split('\n')[0]
	for c in codebook:
		enc2 = encPlain(c).decode()
		enc2 = enc2.split('Result: ')[1].split('\n')[0]
		if enc1 == enc2:
			flag = c + flag
			count += 1
			break;

p.close()

print("------------------------------------------------------\n\n")
print(flag)
print("\n\n------------------------------------------------------")
