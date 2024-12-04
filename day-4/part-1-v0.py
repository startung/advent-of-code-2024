from fileinput import input

# from numpy import array


count = 0
lines = []

for line in input():
    lines.append(line.rstrip())

# horizontal
east = " ".join(lines)
horizontal_forward_count = east.count("XMAS")
count += horizontal_forward_count

# horizontal backwards
horizontal_backward_count = east.count("SAMX")
count += horizontal_backward_count

# vertical
vertical = map("".join, list(zip(*lines)))
south = " ".join(vertical)
vertical_forward_count = south.count("XMAS")
count += vertical_forward_count

# vertical backwards
vertical_backward_count = south.count("SAMX")
count += vertical_backward_count

# diagonal NE
northeast = ""

for i in range(len(lines)):
    for j in range(i + 1):
        northeast += lines[i - j][j]
    northeast += " "

for i in range(len(lines), 1, -1):
    for j in range(1, i):
        northeast += lines[len(lines) - j][10 - (i - j)]
    northeast += " "

diagonal_ne_forward_count = northeast.count("XMAS")
count += diagonal_ne_forward_count

# diagonal NE backwards
diagonal_ne_backward_count = northeast.count("SAMX")
count += diagonal_ne_backward_count

# diagonal SE
southeast = ""
# 9 0
# 8 0, 9 1
# 7 0, 8 2, 7 3
for i in range(len(lines)):
    for j in range(i, 0, -1):
        # print(f"{len(lines) - j} {i-j}", end=", ")
        southeast += lines[len(lines) - j][i - j]
    # print()
    southeast += " "

for i in range(len(lines)):
    southeast += lines[i][i]
southeast += " "
# 0 1, 1 2, 2 3, ...
# 0 2, 1 3, 2 4, ...
# ...
# 0 8, 1 9
# 0 9
for i in range(len(lines), 1, -1):
    for j in range(i - 1):
        # print(f"{j} {len(lines) - i + 1 + j}", end=", ")
        southeast += lines[j][len(lines) - i + 1 + j]
    # print()
    southeast += " "

diagonal_se_forward_count = southeast.count("XMAS")
count += diagonal_se_forward_count

# diagonal SE backwards
diagonal_se_backward_count = southeast.count("SAMX")
count += diagonal_se_backward_count

print(f"wide:{len(line)}, deep:{len(lines)}")
print(f"{horizontal_forward_count=}")
print(f"{horizontal_backward_count=}")
print(f"{vertical_forward_count=}")
print(f"{vertical_backward_count=}")
print(f"{diagonal_ne_forward_count=}")
print(f"{diagonal_ne_backward_count=}")
print(f"{diagonal_se_forward_count=}")
print(f"{diagonal_se_backward_count=}")

print(f"{northeast=}")
print(f"{len(northeast.split())=}")
print(f"{southeast=}")
print(f"{len(southeast.split())=}")

print(count)
