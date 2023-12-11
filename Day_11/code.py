from collections import deque

lines = open("input.txt").read().splitlines()
grid = [list(line) for line in lines]


def expand_grid(grid):
    i = 0
    while i < len(grid):
        if "#" not in grid[i]:
            grid.insert(i, ["."] * len(grid[0]))
            i += 1
        i += 1

    j = 0
    while j < len(grid[0]):
        if all(grid[i][j] != "#" for i in range(len(grid))):
            for row in grid:
                row.insert(j, ".")
            j += 1
        j += 1

    return grid


grid = expand_grid(grid)

# for row in grid:
#     print("".join(row))

# print()


def replace_hashes(grid):
    counter = 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                grid[i][j] = str(counter)
                counter += 1
    return grid


grid = replace_hashes(grid)

# for row in grid:
#     print("".join(row))

numbers = [
    int(grid[i][j])
    for i in range(len(grid))
    for j in range(len(grid[0]))
    if grid[i][j].isdigit()
]
# print(numbers)

# res = [(a, b) for idx, a in enumerate(numbers) for b in numbers[idx + 1 :]]

# print("All possible pairs : " + str(res))
# print(len(res))

positions = {
    (i, j): int(grid[i][j])
    for i in range(len(grid))
    for j in range(len(grid[0]))
    if grid[i][j].isdigit()
}
positions = sorted(positions.items(), key=lambda x: x[1])


def taxicab_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


total_distance = sum(
    taxicab_distance(positions[i][0], positions[j][0])
    for i in range(len(positions))
    for j in range(i + 1, len(positions))
)

print("Part 1:", total_distance)
