import fileinput

list_1, list_2 = [], []
score = 0

for line in fileinput.input():
    input_1, input_2 = line.split()
    list_1.append(int(input_1))
    list_2.append(int(input_2))

for item in list_1:
    score += list_2.count(item) * item

print(score)
