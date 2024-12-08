def multiply_next(position, total, target, fodder):
    if position == len(fodder) and target == total:
        return True
    if position == len(fodder):
        return False
    if fodder[position] * total > target:
        return False
    return add_next(
        position + 1, fodder[position] * total, target, fodder
    ) or multiply_next(position + 1, fodder[position] * total, target, fodder)


def add_next(position, total, target, fodder):
    if position == len(fodder) and target == total:
        return True
    if position == len(fodder):
        return False
    if fodder[position] + total > target:
        return False
    return add_next(
        position + 1, fodder[position] + total, target, fodder
    ) or multiply_next(position + 1, fodder[position] + total, target, fodder)


target = []
fodder = []

with open("input", "r") as f:
    while line := f.readline():
        start, end = line.split(":")
        target.append(int(start))
        fodder.append(list(map(int, end.split())))

    input = f.readlines()

result = 0

for f, t in zip(fodder, target):
    if multiply_next(position=1, total=f[0], target=t, fodder=f) or add_next(
        position=1, total=f[0], target=t, fodder=f
    ):
        result += t


print(result)
