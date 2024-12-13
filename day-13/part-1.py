from dataclasses import dataclass
import numpy as np


@dataclass
class Machine:
    a_dx: int
    a_dy: int
    b_dx: int
    b_dy: int
    prize_x: int
    prize_y: int


machines = []

with open("input", "r") as f:
    while line := f.readline().rstrip():
        button_a = line.rstrip()[10:]
        button_b = f.readline().rstrip()[10:]
        prize = f.readline().rstrip()[7:]
        a_dx, a_dy = button_a.split(", ")
        b_dx, b_dy = button_b.split(", ")
        prize_x, prize_y = prize.split(", ")
        machines.append(
            Machine(
                int(a_dx[2:]),
                int(a_dy[2:]),
                int(b_dx[2:]),
                int(b_dy[2:]),
                int(prize_x[2:]),
                int(prize_y[2:]),
            )
        )
        f.readline()

tokens = 0
cost = np.array([3, 1])

for i, m in enumerate(machines):
    A = np.array([[m.a_dx, m.b_dx], [m.a_dy, m.b_dy]])
    B = np.array([m.prize_x, m.prize_y])
    S = np.linalg.solve(A, B)
    if np.round(np.mod(S[0], 1), 3) in [0, 1] and np.round(np.mod(S[1], 1), 3) in [
        0,
        1,
    ]:  # so awkward due to float to int conversion issues
        tokens += np.sum(S * cost)

print(int(tokens))
