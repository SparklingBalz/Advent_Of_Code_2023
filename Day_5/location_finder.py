seed = [79, 14, 55, 13]

map = [
    [[50, 98, 2], [52, 50, 48]],
    [[0, 15, 37], [37, 52, 2], [39, 0, 15]],
    [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]],
    [[88, 18, 7], [18, 25, 70]],
    [[45, 77, 23], [81, 45, 19], [68, 64, 13]],
    [[0, 69, 1], [1, 0, 69]],
    [[60, 56, 37], [56, 93, 4]],
]


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


print("Locations Map:", min(location(seed, map)))
