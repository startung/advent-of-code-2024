from functools import cache

with open("input", "r") as f:
    stones = list(map(int, f.readline().rstrip().split()))


@cache
def calculate_stones(number, iterations):
    if iterations == 0:
        return 1
    if number == 0:
        return calculate_stones(1, iterations - 1)
    if len(str(number)) % 2 == 0:
        return calculate_stones(
            int(str(number)[: len(str(number)) // 2]), iterations - 1
        ) + calculate_stones(int(str(number)[len(str(number)) // 2 :]), iterations - 1)
    return calculate_stones(number * 2024, iterations - 1)


iterations = 75
total = 0
for stone in stones:
    total += calculate_stones(stone, iterations)

print(total)
