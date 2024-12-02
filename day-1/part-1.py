import fileinput

list_1, list_2 = [], []

for line in fileinput.input():
    input_1, input_2 = line.split()
    list_1.append(int(input_1))
    list_2.append(int(input_2))

print(sum([abs(x - y) for x, y in zip(sorted(list_1), sorted(list_2))]))
