import sys
import numpy as np
from scipy.optimize import linprog


def solve(line):
    if not line.strip():
        return 0

    parts = line.strip().split()

    try:
        target_part = next(p for p in parts if p.startswith("{"))
    except StopIteration:
        return 0

    target_vals = [int(x) for x in target_part.strip("{}").split(",")]
    n_counters = len(target_vals)
    b = np.array(target_vals)

    buttons = []
    for p in parts:
        if p.startswith("("):
            indices = [int(x) for x in p.strip("()").split(",") if x]
            col = [0] * n_counters
            for idx in indices:
                if idx < n_counters:
                    col[idx] = 1
            buttons.append(col)

    if not buttons:
        return 0

    A = np.array(buttons).T
    n_vars = A.shape[1]

    c = np.ones(n_vars)

    res = linprog(c, A_eq=A, b_eq=b, bounds=(0, None), method="highs", integrality=1)

    if res.success:
        return int(np.round(np.sum(res.x)))
    else:
        print(f"Warning: No solution found for line: {line[:30]}...")
        return float("inf")


input_data = sys.stdin.read().strip().split("\n")
total = 0

for line in input_data:
    result = solve(line)
    total += result

print(total)
