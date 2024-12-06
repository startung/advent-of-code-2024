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

direction = "N"
distinct_positions = 2

while not (
    guard_position[0] == 0
    or guard_position[0] == len(maze) - 1
    or guard_position[1] == 0
    or guard_position[1] == len(maze[1]) - 2
):
    print(direction, guard_position)
    x, y = guard_position
    if maze[y][x] == ".":
        maze[y] = maze[y][:x] + "X" + maze[y][x + 1 :]
        distinct_positions += 1
    match direction:
        case "N":
            if maze[y - 1][x] == "#":
                direction = "E"
            else:
                guard_position = (x, y - 1)
        case "E":
            if maze[y][x + 1] == "#":
                direction = "S"
            else:
                guard_position = (x + 1, y)
        case "S":
            if maze[y + 1][x] == "#":
                direction = "W"
            else:
                guard_position = (x, y + 1)
        case "W":
            if maze[y][x - 1] == "#":
                direction = "N"
            else:
                guard_position = (x - 1, y)

for line in maze:
    print(line.rstrip())

print(distinct_positions)
