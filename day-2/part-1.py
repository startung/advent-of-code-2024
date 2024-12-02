import fileinput

safe_count = 0

for report in fileinput.input():
    levels = map(int, report.split())
    levels = list(map(int, report.split()))
    increasing = levels[0] < levels[1]
    problem_dampener_activatated = False
    for current, next in zip(levels[:-1], levels[1:]):
        difference = next - current if increasing else current - next
        if difference <= 0 or difference > 3:
            break
    else:
        safe_count += 1

print(safe_count)
