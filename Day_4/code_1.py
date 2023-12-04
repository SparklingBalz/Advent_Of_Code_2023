def calculate_points(card_strings):
    total_sum = 0

    for card_string in card_strings:
        card_string = card_string.split(":", 1)[-1].strip()

        # print("Card string: ", card_string)

        left_side, right_side = card_string.split("|")

        left_numbers = set(int(num) for num in left_side.split())
        right_numbers = set(int(num) for num in right_side.split())

        # print("Left numbers: ", left_numbers)
        # print("Right numbers: ", right_numbers)

        matching_numbers = left_numbers & right_numbers

        # print("Matching numbers: ", matching_numbers)

        last_value = 0
        for index, _ in enumerate(matching_numbers):
            last_value = 2**index
        total_sum += last_value

    return total_sum


with open("input.txt") as f:
    card_strings = f.read().splitlines()
print("Accumulated points:", calculate_points(card_strings))
