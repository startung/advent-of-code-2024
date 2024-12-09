from collections import defaultdict
from itertools import combinations
from colorama import Fore

antennas = defaultdict(list)
file = "example"
with open(file, "r") as f:
    for y, line in enumerate(f.readlines()):
        for x, frequency in enumerate(line.rstrip()):
            if frequency != ".":
                antennas[frequency].append([x, y])

height, width = y + 1, x + 1
print(height, width)

# print(antennas)

antinodes = set()
antinode_count = 0

for key, antennas in antennas.items():
    for pair in combinations(antennas, 2):
        dx, dy = pair[0][0] - pair[1][0], pair[0][1] - pair[1][1]
        dx_p, dy_p = dx, dy
        dx_n, dy_n = dx, dy
        while (
            pair[0][0] + dx_p >= 0
            and pair[0][0] + dx_p < width
            and pair[0][1] + dy_p >= 0
            and pair[0][1] + dy_p < height
        ):
            antinodes.add((pair[0][0] + dx_p, pair[0][1] + dy_p, key))
            dx_p += dx
            dy_p += dy
        while (
            pair[1][0] - dx_n >= 0
            and pair[1][0] - dx_n < width
            and pair[1][1] - dy_n >= 0
            and pair[1][1] - dy_n < height
        ):
            antinodes.add((pair[1][0] - dx_n, pair[1][1] - dy_n, key))
            dx_n += dx
            dy_n += dy
        antinodes.add((*pair[0], key))
        antinodes.add((*pair[1], key))

        # print(pair, dx, dy, (pair[0][0] + dx, pair[0][1] + dy))
    # break


def print_antinode(x, y, key):
    with open(file, "r") as f:
        for row, line in enumerate(f.readlines()):
            line = line.replace(".", "⸱")
            line = line.replace(key, Fore.YELLOW + key + Fore.RESET)
            if row == y:
                line = line[:x] + Fore.RED + "#" + Fore.RESET + line[x + 1 :]
            print(line.rstrip())
    input()


grid = []
with open(file, "r") as f:
    for row, line in enumerate(f.readlines()):
        line = line.rstrip().replace(".", "⸱")
        grid.append(line)

for antinode in antinodes:
    x, y, _ = antinode
    grid[y] = grid[y][:x] + "#" + grid[y][x + 1 :]

for line in grid:
    print(line)


# for i, antinode in enumerate(antinodes):
#     print(Fore.GREEN + str(i) + Fore.RESET + ":", *antinode)
#     print_antinode(*antinode)

unique_antinodes = set((x, y) for x, y, _ in antinodes)

print(len(unique_antinodes))
