def winning_numbers(card):
    card_string = card.split(":", 1)[-1].strip()

    left_side, right_side = card_string.split("|")

    left_numbers = set(int(num) for num in left_side.split())
    right_numbers = set(int(num) for num in right_side.split())

    matching_numbers = left_numbers & right_numbers

    return matching_numbers


with open("input.txt") as f:
    card_strings = f.read().splitlines()

card_copies = [1] * len(card_strings)
for i, card in enumerate(card_strings):
    winning = winning_numbers(card)
    if winning:
        for j in range(1, len(winning) + 1):
            card_copies[i + j] += card_copies[i]

print("Total cards:", sum(card_copies))
