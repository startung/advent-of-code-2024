topo_map = []
trailheads = []

with open("input", "r") as f:
    while line := f.readline():
        topo_map.append([int(x) for x in line.rstrip()])

for y, line in enumerate(topo_map):
    for x, height in enumerate(line):
        if height == 0:
            trailheads.append((x, y))
    print(line)

print(trailheads)


def walk(topo_map, pos: tuple[int]):
    x, y = pos[0], pos[1]
    height = topo_map[y][x]
    if height == 9:
        return 1
    reached = 0
    if y > 0 and topo_map[y][x] + 1 == topo_map[y - 1][x]:  # go north
        reached += walk(topo_map, (x, y - 1))
    if x < len(topo_map[0]) - 1 and topo_map[y][x] + 1 == topo_map[y][x + 1]:  # east
        reached += walk(topo_map, (x + 1, y))
    if y < len(topo_map) - 1 and topo_map[y][x] + 1 == topo_map[y + 1][x]:  # south
        reached += walk(topo_map, (x, y + 1))
    if x > 0 and topo_map[y][x] + 1 == topo_map[y][x - 1]:  # west
        reached += walk(topo_map, (x - 1, y))
    return reached


result = 0
for pos in trailheads:
    result += walk(topo_map, pos)

print(result)
