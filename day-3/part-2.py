import fileinput
from re import findall

result = 0

lines = ""

for line in fileinput.input():
    lines += line + " "

do = ""
while True:
    lines = lines.split("don't()", 1)
    do += lines[0]
    if len(lines) < 2:
        break
    lines = lines[1].split("do()", 1)[1]

multiplications = findall(r"mul\(\d{1,3},\d{1,3}\)", do)

for m in multiplications:
    pair = map(int, m[4:-1].split(","))
    result += next(pair) * next(pair)

print(result)
