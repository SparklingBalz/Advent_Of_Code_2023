# import re, math

import re, math


def find_grouped_numbers(grid):
    row_length = grid.index("\n") + 1
    numbers = [
        (int(match.group()), set(range(match.span()[0], match.span()[1])))
        for match in re.finditer("\d+", grid)
    ]
    symbols = {
        match.span()[0] + delta
        for match in re.finditer("[^0-9.\n]", grid)
        for delta in (
            -row_length - 1,
            -row_length,
            -row_length + 1,
            -1,
            1,
            row_length - 1,
            row_length,
            row_length + 1,
        )
    }
    gears = [
        {
            match.span()[0] + delta
            for delta in (
                -row_length - 1,
                -row_length,
                -row_length + 1,
                -1,
                1,
                row_length - 1,
                row_length,
                row_length + 1,
            )
        }
        for match in re.finditer("\*", grid)
    ]
    part1 = sum(n for n, p in numbers if p & symbols)
    part2 = sum(
        math.prod(gn) if len(gn := [n for n, p in numbers if p & gear]) == 2 else 0
        for gear in gears
    )
    return part1, part2


with open("input.txt") as f:
    grid = f.read()
print(f"Part 1: {find_grouped_numbers(grid)}")
