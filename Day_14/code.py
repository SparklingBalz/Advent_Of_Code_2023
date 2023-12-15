def move_O_up(input_grid):
    rows, cols = len(input_grid), len(input_grid[0])

    grid = [list(row) for row in input_grid]

    for col in range(cols):
        for row in range(1, rows):
            if grid[row][col] == "O":
                while (row > 0) and (
                    grid[row - 1][col] == "." or grid[row - 1][col] == "O"
                ):
                    grid[row][col], grid[row - 1][col] = (
                        grid[row - 1][col],
                        grid[row][col],
                    )
                    row -= 1

    return grid


def print_output(output_grid):
    for row in output_grid:
        print("".join(row))


input_data = open("input.txt", "r").read().splitlines()
output_data = move_O_up(input_data)

# print_output(output_data)


def get_o_positions(grid):
    rows, cols = len(grid), len(grid[0])
    o_positions = {col: [] for col in range(cols)}

    for col in range(cols):
        for row in range(rows - 1, -1, -1):
            if grid[row][col] == "O":
                o_positions[col].append(rows - row)

    return o_positions


o_positions = get_o_positions(output_data)
# print(o_positions)

sum_o_positions = {col: sum(positions) for col, positions in o_positions.items()}
total_sum = sum(sum_o_positions.values())
print("Part 1:", total_sum)
