from collections import defaultdict
from itertools import combinations
from colorama import Fore

antennas = defaultdict(list)
file = "input"
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
        if (
            pair[0][0] + dx >= 0
            and pair[0][0] + dx < width
            and pair[0][1] + dy >= 0
            and pair[0][1] + dy < height
        ):
            antinodes.add((pair[0][0] + dx, pair[0][1] + dy, key))
        if (
            pair[1][0] - dx >= 0
            and pair[1][0] - dx < width
            and pair[1][1] - dy >= 0
            and pair[1][1] - dy < height
        ):
            antinodes.add((pair[1][0] - dx, pair[1][1] - dy, key))

        # print(pair, dx, dy, (pair[0][0] + dx, pair[0][1] + dy))
    # break


def print_antenode(x, y, key):
    with open(file, "r") as f:
        for row, line in enumerate(f.readlines()):
            line = line.replace(".", "⸱")
            line = line.replace(key, Fore.YELLOW + key + Fore.RESET)
            if row == y:
                line = line[:x] + Fore.RED + "#" + Fore.RESET + line[x + 1 :]
            print(line.rstrip())
    input()


# for i, antinode in enumerate(antinodes):
#     print(Fore.GREEN + str(i) + Fore.RESET + ":", *antinode)
#     print_antenode(*antinode)

unique_antinodes = set((x, y) for x, y, _ in antinodes)

print(len(unique_antinodes))
