caesar_list = "nmlkjihgfedcbazyxwvutsrqpo"
alpha_list = "abcdefghijklmnopqrstuvwxyz"

param1 = input("Enter param1: ")
param2 = ""

for c in param1:
    index = 0
    for a in caesar_list:
        if a == c:
            break
        index += 1
    temp = index
    index += 10
    if (0x19 < index):
        index = temp - 0x10
    print(index)
    param2 += caesar_list[index]

print(f"Param2: {param2}")
