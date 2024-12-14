from dataclasses import dataclass

robots = []
width, height = 101, 103


@dataclass
class Robot:
    x: int
    y: int
    dx: int
    dy: int


def display_robots(robots: list[Robot]) -> None:
    space = [[0 for _ in range(width)] for _ in range(height)]
    for r in robots:
        space[r.y][r.x] += 1
    for line in space:
        print("".join([" " if x == 0 else str(x) for x in line]))
    print()


with open("input", "r") as f:
    while line := f.readline():
        line = line.rstrip().split(" ")
        p = line[0][2:].split(",")
        v = line[1][2:].split(",")
        robots.append(Robot(int(p[0]), int(p[1]), int(v[0]), int(v[1])))

display_robots(robots)

i = 1
while True:
    # vertical: 917, 1018, 1119 (101   11*101 + 8)
    # horizontal: 1005, 1108, 1211 (103  11*103 -25)
    for r in robots:
        r.x = (r.x + r.dx) % width
        r.y = (r.y + r.dy) % height
    if (i - 8) % 101 == 0 or (i + 25) % 103 == 0:
        print(
            "------------------------------------",
            i,
            "------------------------------------",
        )
        display_robots(robots)
        key = input()
        if key == "e":
            break
    i += 1
