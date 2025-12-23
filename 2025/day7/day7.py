from collections import defaultdict


with open("input.txt", "r") as f:
    grid = [line.rstrip("\n\r") for line in f]


# 1. Find the starting position 'S'
start_x, start_y = -1, -1
for y, row in enumerate(grid):
    if "S" in row:
        start_y = y
        start_x = row.find("S")
        break

# assuming start_y != -1
active_paths = {start_x: 1}

for y in range(start_y, len(grid)):
    next_paths = defaultdict(int)
    current_row = grid[y]
    row_len = len(current_row)

    for x, count in active_paths.items():
        if 0 <= x < row_len and current_row[x] == "^":
            next_paths[x - 1] += count
            next_paths[x + 1] += count
        else:
            next_paths[x] += count

    active_paths = next_paths

answer = sum(active_paths.values())
print(answer)
