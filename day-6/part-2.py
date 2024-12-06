from copy import deepcopy
from tqdm import tqdm

maze = []
with open("input", "r") as f:
    maze = f.readlines()

obstructions = []
guard_position = (0, 0)

for y, line in enumerate(maze):
    x = line.find("^")
    if x >= 0:
        guard_position = (x, y)
    obstructions.extend([(x, y) for x, c in enumerate(line) if c == "#"])

x, y = guard_position
maze[y] = maze[y][:x] + "X" + maze[y][x + 1 :]


def solve_maze(direction, x, y, maze):
    direction = "N"
    distinct_positions = 2
    log = []
    while not (x == 0 or x == len(maze) - 1 or y == 0 or y == len(maze[1]) - 2):
        if (direction, x, y) in log:
            return -1
        else:
            log.append((direction, x, y))
        if maze[y][x] == ".":
            maze[y] = maze[y][:x] + "X" + maze[y][x + 1 :]
            distinct_positions += 1
        match direction:
            case "N":
                if maze[y - 1][x] == "#":
                    direction = "E"
                else:
                    y = y - 1
            case "E":
                if maze[y][x + 1] == "#":
                    direction = "S"
                else:
                    x = x + 1
            case "S":
                if maze[y + 1][x] == "#":
                    direction = "W"
                else:
                    y = y + 1
            case "W":
                if maze[y][x - 1] == "#":
                    direction = "N"
                else:
                    x = x - 1
    return distinct_positions


count = 0

for y, line in enumerate(tqdm(maze)):
    for x, spot in enumerate(line):
        if spot == ".":
            tmp_maze = deepcopy(maze)
            tmp_maze[y] = maze[y][:x] + "#" + maze[y][x + 1 :]
            result = solve_maze("N", guard_position[0], guard_position[1], tmp_maze)
            if result == -1:
                count += 1

print(count)
