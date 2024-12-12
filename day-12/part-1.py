from collections import defaultdict

plants = defaultdict(int)
grid = []
with open("input", "r") as f:
    while line := f.readline():
        grid.append(list(line.rstrip()))
        for c in line.rstrip():
            plants[c] += 1


def find_region(x, y):
    plant = grid[y][x]
    area = 1
    perimeter = 4
    grid[y][x] = grid[y][x].lower()
    if y > 0 and plant == grid[y - 1][x]:  # go north
        adjacent_area, adjacent_perimeter = find_region(x, y - 1)
        area += adjacent_area
        if adjacent_area > 0:
            perimeter += adjacent_perimeter
    if y > 0 and grid[y - 1][x] == grid[y][x].lower():
        perimeter -= 1
    if x < len(grid[0]) - 1 and plant == grid[y][x + 1]:  # east
        adjacent_area, adjacent_perimeter = find_region(x + 1, y)
        area += adjacent_area
        if adjacent_area > 0:
            perimeter += adjacent_perimeter
    if x < len(grid[0]) - 1 and grid[y][x + 1] == grid[y][x].lower():
        perimeter -= 1
    if y < len(grid) - 1 and plant == grid[y + 1][x]:  # south
        adjacent_area, adjacent_perimeter = find_region(x, y + 1)
        area += adjacent_area
        if adjacent_area > 0:
            perimeter += adjacent_perimeter
    if y < len(grid) - 1 and grid[y + 1][x] == grid[y][x].lower():
        perimeter -= 1
    if x > 0 and plant == grid[y][x - 1]:  # west
        adjacent_area, adjacent_perimeter = find_region(x - 1, y)
        area += adjacent_area
        if adjacent_area > 0:
            perimeter += adjacent_perimeter
    if x > 0 and grid[y][x - 1] == grid[y][x].lower():
        perimeter -= 1
    return area, perimeter


for line in grid:
    print("".join(line))

print("\nIt contains:\n")

total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if not grid[y][x].islower():
            area, perimeter = find_region(x, y)
            print(
                f"A region of R plants with price {area} * {perimeter} = {area*perimeter}."
            )
            total += area * perimeter

print(f"So, it has a total price of {total}.")
