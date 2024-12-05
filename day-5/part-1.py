from collections import defaultdict

to_print = []
ordering_rules = defaultdict(set)

with open("input", "r") as f:
    while line := f.readline().rstrip():
        before, page = line.split("|")
        ordering_rules[page].add(before)
    while line := f.readline().rstrip():
        to_print.append(line.split(","))

middle_pages = 0

for update in to_print:
    for idx, page in enumerate(update[:-1]):
        if set(update[idx + 1 :]).intersection(ordering_rules[page]):
            break
    else:
        middle_pages += int(update[len(update) // 2])
print(middle_pages)
