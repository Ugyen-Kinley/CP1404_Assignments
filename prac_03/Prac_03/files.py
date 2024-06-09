name = input("Enter your name: ")
name_of_file = open("name.txt", "w")
name_of_file.write(name)
name_of_file.close()

name_of_file = open("name.txt", "r")
name = name_of_file.read().strip()
name_of_file.close()
print(f"Hi {name}!")

with open("numbers.txt", "w") as numbers_file:
    numbers_file.write("17\n42\n400\n")

with open("numbers.txt", "r") as numbers_file:
    the_first_number = int(numbers_file.readline())
    the_second_number = int(numbers_file.readline())
result = the_first_number + the_second_number
print(result)

total = 0
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        total += int(line)
print(total)
