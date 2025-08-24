from pwn import *

flag = ""
count = 0
test_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.-{}"

p = process("/challenge/run")

def encPlain(c):
	p.write(b'1\n')
	p.read()
	p.write(flag.encode() + c.encode() + b'\n')

	return p.read()

def encFlag():
	p.write(b'2\n')
	p.read()
	p.write(b'0\n')
	p.read()
	p.write(str(count + 1).encode() + b'\n')

	return p.read()

p.read()
while(True):
	print(flag)
	enc2 = encFlag().decode()
	enc2 = enc2.split('Result: ')[1].split('\n')[0]
	for c in test_string:
		enc1 = encPlain(c).decode()
		enc1 = enc1.split('Result: ')[1].split('\n')[0]
		if enc1 == enc2:
			flag += c
			count += 1
			break;

	if (flag[0] == 'p' and flag[-1] == '}'):
		p.close()
		break;

print("------------------------------------------------------\n\n")
print(flag)
print("\n\n------------------------------------------------------")

