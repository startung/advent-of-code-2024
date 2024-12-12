with open("example", "r") as f:
    stones = list(map(int, f.readline().rstrip().split()))

iterations = 25

for idx, _ in enumerate(range(iterations)):
    print(idx, len(stones))
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            new_stones.extend(
                [
                    int(str(stone)[: len(str(stone)) // 2]),
                    int(str(stone)[len(str(stone)) // 2 :]),
                ]
            )
        else:
            new_stones.append(stone * 2024)
    stones = new_stones
print(iterations, len(stones))
