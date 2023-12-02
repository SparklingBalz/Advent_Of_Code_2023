import re

# def check_colors(s):
#     total_blue = total_red = total_green = 0

#     matches = re.findall(r'(\d+)\s*(blue|red|green)', s)
#     for match in matches:
#         count, color = match
#         if color == 'blue':
#             total_blue += int(count)
#         elif color == 'red':
#             total_red += int(count)
#         elif color == 'green':
#             total_green += int(count)

#     return total_blue <= 14 and total_red <= 12 and total_green <= 13

# s = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
# print(check_colors(s))

import re


def check_colors(s):
    total_blue = total_red = total_green = 0

    matches = re.findall(r"(\d+)\s*(blue|red|green)", s)

    for match in matches:
        count, color = match
        if color == "blue":
            if int(count) > 14:
                return None
        elif color == "red":
            if int(count) > 12:
                return None
        elif color == "green":
            if int(count) > 13:
                return None

    return re.search(r"Game (\d+):", s).group(1)


with open("input.txt") as f:
    games = f.read().splitlines()

valid_ids = []
for game in games:
    game_id = check_colors(game)
    if game_id is not None:
        valid_ids.append(int(game_id))

print(valid_ids)
print("Sum od all IDs: ", sum(valid_ids))
