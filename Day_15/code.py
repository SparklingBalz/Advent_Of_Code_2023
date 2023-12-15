strings = open("input.txt").read().split(",")
values = []

for string in strings:
    current_value = 0
    for char in string:
        current_value = (current_value + ord(char)) * 17 % 256
    values.append(current_value)

print("Part 1:", sum(values))
