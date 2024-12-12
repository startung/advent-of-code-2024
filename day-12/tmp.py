grid = []
with open("input", "r") as f:
    while line := f.readline():
        grid.append(list(line.rstrip()))

height, width = len(grid), len(grid[0])


def find_area(x, y):
    plant = grid[y][x]
    area = 1
    grid[y][x] = plant.lower()
    tmp_grid[x + 1][y + 1] = plant
    if y > 0 and plant == grid[y - 1][x]:  # go north
        area += find_area(x, y - 1)
    if x < len(grid[0]) - 1 and plant == grid[y][x + 1]:  # east
        area += find_area(x + 1, y)
    if y < len(grid) - 1 and plant == grid[y + 1][x]:  # south
        area += find_area(x, y + 1)
    if x > 0 and plant == grid[y][x - 1]:  # west
        area += find_area(x - 1, y)
    return area


def find_vertices(tmp_grid):
    height, width = len(tmp_grid), len(tmp_grid[0])

    vertices = 0
    for y in range(height - 1):
        for x in range(width - 1):
            if (
                tmp_grid[y][x] == tmp_grid[y][x + 1]
                and tmp_grid[y + 1][x] == tmp_grid[y + 1][x + 1]
            ) or (
                tmp_grid[y][x] == tmp_grid[y + 1][x]
                and tmp_grid[y][x + 1] == tmp_grid[y + 1][x + 1]
            ):
                continue
            elif (
                len(
                    set(
                        [
                            tmp_grid[y][x],
                            tmp_grid[y][x + 1],
                            tmp_grid[y + 1][x],
                            tmp_grid[y + 1][x + 1],
                        ]
                    )
                )
                == 3
            ):
                vertices += 2
            elif (
                tmp_grid[y][x] == tmp_grid[y + 1][x + 1]
                and tmp_grid[y + 1][x] == tmp_grid[y][x + 1]
            ):
                vertices += 2
            else:
                vertices += 1

    return vertices


for line in grid:
    print("".join(line))


print("\nIt contains:\n")

total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if not grid[y][x].islower():
            tmp_grid = [["*" for _ in range(width + 2)] for _ in range(height + 2)]
            area = find_area(x, y)
            sides = find_vertices(tmp_grid)
            print(f"A region of R plants with price {area} * {sides} = {area*sides}.")
            total += area * sides
    #     break
    # break

print(f"So, it has a total price of {total}.")
