from collections import defaultdict
from ordered_set import OrderedSet

to_print = []
ordering_rules = defaultdict(OrderedSet)

with open("input", "r") as f:
    while line := f.readline().rstrip():
        before, page = line.split("|")
        ordering_rules[page].add(before)
    while line := f.readline().rstrip():
        to_print.append(line.split(","))


def correct_order(update):
    for idx, page in enumerate(update[:-1]):
        if set(update[idx + 1 :]).intersection(ordering_rules[page]):
            return False
    return True


def reorder(update):
    for idx, page in enumerate(update[:-1]):
        wrong_pages = OrderedSet(update[idx + 1 :]).intersection(ordering_rules[page])
        if wrong_pages:
            update.insert(update.index(wrong_pages[-1]) + 1, update[idx])
            update[idx] = 0
    return [x for x in update if x != 0]


middle_pages = 0

for update in to_print:
    wrong_order = not correct_order(update)
    while not correct_order(update):
        update = reorder(update)

    if wrong_order:
        middle_pages += int(update[len(update) // 2])

print(middle_pages)
