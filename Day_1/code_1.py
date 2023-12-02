with open("input.txt") as f:
    strings_list = f.read().splitlines()

# strings_list = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "trebuchet"]

total = 0
numbers_list = []
joined_numbers_list = []
for string in strings_list:
    numbers = [i for i in string if i.isdigit()]
    if not numbers:
        continue
    numbers_list.append(numbers)

for numbers in numbers_list:
    numbers = [numbers[0], numbers[-1]]
    joined_number = int("".join(numbers))
    joined_numbers_list.append(joined_number)

total = sum(joined_numbers_list)

print(total)
