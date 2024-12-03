import fileinput
from re import findall

result = 0

for line in fileinput.input():
    multiplications = findall(r"mul\(\d{1,3},\d{1,3}\)", line)

    for m in multiplications:
        pair = map(int, m[4:-1].split(","))
        result += next(pair) * next(pair)

print(result)
