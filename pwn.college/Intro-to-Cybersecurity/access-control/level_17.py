from pwn import *

p = process("/challenge/run")

Levels = {"TS": 4, "S": 3, "UC": 2, "C": 1}

for i in range(21):
	p.recvline()

def Dom(Level, Level_Prime, Category, Category_Prime):
	if Level_Prime <= Level and set(Category_Prime) <= set(Category):
		return True
	return False

for i in range(20):
	question = p.recvline().decode()
	print(question)
	Level = Levels[question.split("level ")[1].split(" and")[0]]
	print(Level)
	Level_Prime = Levels[question.split("level ")[2].split(" and")[0]]
	print(Level_Prime)

	Category = question.split("categories {")[1].split("} ")[0].split(", ")
	print(Category)
	Category_Prime = question.split("categories {")[2].split("}?")[0].split(", ")
	print(Category_Prime)

	Write_Read = question.split("} ")[1].split()[0]
	print(Write_Read)

	if Write_Read == "read":
		if Dom(Level, Level_Prime, Category, Category_Prime):
			p.write("yes\n")
			print("yes")
		else:
			p.write("no\n")
			print("no")
	else:
		if Dom(Level_Prime, Level, Category_Prime, Category):
			p.write("yes\n")
			print("yes")
		else:
			p.write("no\n")
			print("no")
	print(p.recvline())

print(p.read())

#	L = Security_Level[question[7].decode()]
#	L_prime = Security_Level[question[].decode()]
