from pwn import *

p = process("/challenge/run")

def recv_until_target(proc, target):
    while True:
        line = proc.recvline().decode('utf-8').strip()  # Read one line
        print(f"Received: {line}")  # For debugging purposes
        if line == target:
            break
    print("Target line received!")

recv_until_target(p, "40 Levels (first is highest aka more sensitive):")

Levels = dict()
for i in range(40, 0, -1):
	Levels[p.recvline().rstrip(b"\n").decode()] = i
print(Levels)

for i in range(6):
	p.recvline()

def Dom(Level, Level_Prime, Category, Category_Prime):
	print(f"L' <= L = {Level_Prime <= Level}")
	print(f"C' <= C = {set(Category_Prime).issubset(set(Category))}")
	print(set(Category_Prime))
	print(set(Category))
	if Level_Prime <= Level and set(Category_Prime).issubset(set(Category)):
		return True
	return False

for i in range(128):
	question = p.recvline().decode()
	print(question)
	Level1 = Levels[question.split("level ")[1].split(" and")[0]]
	print(f"Level 1: {Level1}")
	Level2 = Levels[question.split("level ")[2].split(" and")[0]]
	print(f"Level 2: {Level2}")

	Category1 = question.split("categories {")[1].split("} ")[0].split(", ")
	print(f"Category 1: {Category1}")
	Category1.append("")
	Category2 = question.split("categories {")[2].split("}?")[0].split(", ")
	print(f"Category 2: {Category2}")
	Category2.append("")

	Write_Read = question.split("} ")[1].split()[0]
	print(f"Write or Read: {Write_Read}")

	if Write_Read == "read":
		if Dom(Level1, Level2, Category1, Category2):
			p.write("yes\n")
			print("yes")
		else:
			p.write("no\n")
			print("no")
		print("Dom(Level1, Level2, Category1, Category2)")
	else:
		if Dom(Level2, Level1, Category2, Category1):
			p.write("yes\n")
			print("yes")
		else:
			p.write("no\n")
			print("no")
			print("Dom(Level2, Level1, Category2, Category1)")

	print(p.recvline())

print(p.read())

#	L = Security_Level[question[7].decode()]
#	L_prime = Security_Level[question[].decode()]
