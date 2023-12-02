import re


def check_colors(s):
    total_blue = total_red = total_green = 0

    matches = re.findall(r"(\d+)\s*(blue|red|green)", s)

    for match in matches:
        count, color = match
        if color == "blue":
            if total_blue < int(count):
                total_blue = int(count)
        elif color == "red":
            if total_red < int(count):
                total_red = int(count)
        elif color == "green":
            if total_green < int(count):
                total_green = int(count)

    return total_red * total_blue * total_green


with open("input.txt") as f:
    games = f.read().splitlines()

valid_ids = []
for game in games:
    game_id = check_colors(game)
    valid_ids.append(game_id)
#     if game_id is not None:
#         valid_ids.append(int(game_id))

# print(valid_ids)
print("Sum od all IDs: ", sum(valid_ids))
