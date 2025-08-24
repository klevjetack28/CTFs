start_000 = ""
start_666 = ""
middle_00 = ""
end_0000 = ""

with open("ssn.txt", "r") as file:
    for line in file:
        numbers = line.split("-")
        
        if numbers[0] == "000":
            start_000 = line
        elif numbers[0] == "666":
            start_666 = line
        elif numbers[1] == "00":
            middle_00 = line
        elif numbers[2] == "0000":
            end_0000 = line

print(f"Start_000: {start_000}")
print(f"Start_666: {start_666}")
print(f"Middle_00: {middle_00}")
print(f"End_0000: {end_0000}")
