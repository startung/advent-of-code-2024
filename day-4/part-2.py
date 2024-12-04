from fileinput import input

grid = []

for line in input():
    grid.append(line.rstrip())

count = 0
for i in range(len(grid) - 2):
    for j in range(len(grid[0]) - 2):
        count += "".join([grid[i + 2][j], grid[i + 1][j + 1], grid[i + 0][j + 2]]) in [
            "MAS",
            "SAM",
        ] and "".join([grid[i][j], grid[i + 1][j + 1], grid[i + 2][j + 2]]) in [
            "MAS",
            "SAM",
        ]

print(count)
