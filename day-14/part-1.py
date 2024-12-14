from dataclasses import dataclass

robots = []
width, height = 101, 103


@dataclass
class Robot:
    x: int
    y: int
    dx: int
    dy: int


with open("input", "r") as f:
    while line := f.readline():
        line = line.rstrip().split(" ")
        p = line[0][2:].split(",")
        v = line[1][2:].split(",")
        robots.append(Robot(int(p[0]), int(p[1]), int(v[0]), int(v[1])))


for _ in range(100):
    for r in robots:
        r.x = (r.x + r.dx) % width
        r.y = (r.y + r.dy) % height


quadrants = [0, 0, 0, 0]

for r in robots:
    if r.x < width // 2 and r.y < height // 2:
        quadrants[0] += 1
    if r.x > width // 2 and r.y < height // 2:
        quadrants[1] += 1
    if r.x < width // 2 and r.y > height // 2:
        quadrants[2] += 1
    if r.x > width // 2 and r.y > height // 2:
        quadrants[3] += 1


print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])
