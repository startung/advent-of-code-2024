from fileinput import input

count = 0
lines = []


def print_grid(grid):
    for row in grid:
        print(row)


def check_4x4(grid):
    return sum(
        (
            sum([x == "XMAS" for x in grid]),  # horizontal forward
            sum([x == "SAMX" for x in grid]),  # horizontal backward
            sum(
                [x == "XMAS" for x in list(map("".join, list(zip(*grid))))]
            ),  # vertical forward
            sum(
                [x == "SAMX" for x in list(map("".join, list(zip(*grid))))]
            ),  # vertical backward
            "".join([grid[3][0], grid[2][1], grid[1][2], grid[0][3]])
            == "XMAS",  # diagonal NE forward
            "".join([grid[3][0], grid[2][1], grid[1][2], grid[0][3]])
            == "SAMX",  # diagonal NE backward
            "".join([grid[0][0], grid[1][1], grid[2][2], grid[2][2]])
            == "XMAS",  # diagonal SE forward
            "".join([grid[0][0], grid[1][1], grid[2][2], grid[2][2]])
            == "SAMX",  # diagonal SE backward
        )
    )


for line in input():
    lines.append(line.rstrip())

# grid_1hf = ["XMAS", "    ", "    ", "    "]
# grid_1hb = ["SAMX", "    ", "    ", "    "]
# grid_1vf = ["X   ", "M   ", "A   ", "S   "]
# grid_1vb = ["S   ", "A   ", "M   ", "X   "]
# grid_1dnef = ["   S", "  A ", " M  ", "X   "]
# grid_1dneb = ["   X", "  M ", " A  ", "S   "]
# grid_1dsef = ["X   ", " M  ", "  A ", "   S"]
# grid_1dsef = ["S   ", " A  ", "  M ", "   X"]
# count = check_4x4(grid_1dneb)

# print(lines[0])

print_grid(lines)

count = 0

for i in range(len(lines) - 3):
    for j in range(len(lines[0]) - 3):
        grid = [
            lines[i][j : j + 4],
            lines[i + 1][j : j + 4],
            lines[i + 2][j : j + 4],
            lines[i + 3][j : j + 4],
        ]
        print_grid(grid)
        print(check_4x4(grid))
        print()
        count += check_4x4(grid)

print(count)
