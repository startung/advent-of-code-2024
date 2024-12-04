from fileinput import input


def check_horizonal(grid, string):
    return sum([line.count(string) for line in grid])


def check_vertical(grid, string):
    return sum([line.count(string) for line in list(map("".join, list(zip(*grid))))])


def check_diagonal(grid, string):
    count = 0
    for i in range(len(grid) - 3):
        for j in range(len(grid[0]) - 3):
            count += (
                "".join(
                    [
                        grid[i + 3][j],
                        grid[i + 2][j + 1],
                        grid[i + 1][j + 2],
                        grid[i][j + 3],
                    ]
                )
                == string
            )  # diagonal NE
            count += (
                "".join(
                    [
                        grid[i][j],
                        grid[i + 1][j + 1],
                        grid[i + 2][j + 2],
                        grid[i + 3][j + 3],
                    ]
                )
                == string
            )  # diagonal SE
    return count


lines = []

for line in input():
    lines.append(line.rstrip())

count = 0

count += check_horizonal(lines, "XMAS")
count += check_horizonal(lines, "SAMX")
count += check_vertical(lines, "XMAS")
count += check_vertical(lines, "SAMX")
count += check_diagonal(lines, "XMAS")
count += check_diagonal(lines, "SAMX")

print(count)
