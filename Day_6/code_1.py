from functools import reduce
import operator

time = []
distance = []

with open("input.txt", "r") as file:
    time_line = file.readline()
    time += [int(num) for num in time_line.split(":")[1].strip().split()]

    distance_line = file.readline()
    distance += [int(num) for num in distance_line.split(":")[1].strip().split()]

results = []


def get_distance_traveled(time, time_i):
    distance = []
    for time in range(0, time_i):
        distance_traveled = time * (time_i - time)
        distance.append(distance_traveled)
    return distance


def get_possible_ways(distance, distance_1):
    possible_ways = []
    for dist in distance:
        if dist > distance_1:
            possible_ways.append(dist)
    return possible_ways


for time_i, distance_i in zip(time, distance):
    distances = get_distance_traveled(time_i, time_i)
    possible_ways = get_possible_ways(distances, distance_i)
    results.append(len(possible_ways))


product = reduce(operator.mul, results, 1)
print("Part 1:", product)

joined_time = int("".join(str(num) for num in time))
joined_distance = int("".join(str(num) for num in distance))

print(
    "Part 2:",
    len(
        get_possible_ways(
            get_distance_traveled(joined_time, joined_time), joined_distance
        )
    ),
)
