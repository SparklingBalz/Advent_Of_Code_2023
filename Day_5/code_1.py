with open("seed_input.txt") as f:
    seed_input = f.read().splitlines()

with open("input.txt") as f:
    maps = f.read()


def getSeeds(seeds):
    for seed in seeds:
        filtered_seeds = seed.split(":", 1)[-1].strip()
    return list(map(int, filtered_seeds.split()))


def getMaps(maps):
    # map_name = "map"
    numbers = maps.splitlines()[1:]

    numbers_arrays = []
    numbers_array = []
    for line in numbers:
        try:
            line_numbers = list(map(int, line.split()))
            if line_numbers:
                numbers_array.append(line_numbers)
            else:
                if numbers_array:
                    numbers_arrays.append(numbers_array)
                    numbers_array = []
        except ValueError:
            continue

    if numbers_array:
        numbers_arrays.append(numbers_array)

    # for i, numbers_array in enumerate(numbers_arrays):
    #     globals()[f"{map_name}_{i}"] = numbers_array
    #     print(f"{map_name}_{i}:", globals()[f"{map_name}_{i}"])

    return numbers_arrays


def location(seeds, map):
    locations_map = []
    for seed in seeds:
        current_location = seed
        for outer_array in map:
            for sub_array in outer_array:
                if current_location in range(sub_array[1], sub_array[1] + sub_array[2]):
                    current_location = current_location - sub_array[1] + sub_array[0]
                    break
        else:
            locations_map.append(current_location)
    return locations_map


# print("Seeds:", getSeeds(seed_input), "\n")
# print("Maps arrays:", getMaps(maps))
print("Min Location:", min(location(getSeeds(seed_input), getMaps(maps))))
