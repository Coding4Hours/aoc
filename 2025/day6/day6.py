with open("input.txt", "r") as f:
    lines = [line.rstrip("\n\r") for line in f]

max_width = max(len(line) for line in lines)
grid = [line.ljust(max_width) for line in lines]
num_rows = len(grid)

is_content_col = []
for x in range(max_width):
    col_has_content = False
    for y in range(num_rows):
        if grid[y][x].strip():
            col_has_content = True
            break
    is_content_col.append(col_has_content)

problem_ranges = []
start_x = None
for x in range(max_width):
    if is_content_col[x]:
        if start_x is None:
            start_x = x
    else:
        if start_x is not None:
            problem_ranges.append((start_x, x - 1))
            start_x = None
if start_x is not None:
    problem_ranges.append((start_x, max_width - 1))

answer = 0

for start, end in problem_ranges:
    numbers = []

    operator = None
    for x in range(start, end + 1):
        char = grid[num_rows - 1][x]
        if char in ("+", "*"):
            operator = char
            break

    for x in range(start, end + 1):
        column_digits = ""
        for y in range(num_rows - 1):
            char = grid[y][x]
            if char.isdigit():
                column_digits += char

        if column_digits:
            numbers.append(int(column_digits))
        if not numbers or not operator:
            continue

    if operator == "+":
        problem_result = sum(numbers)
    elif operator == "*":
        problem_result = 1
        for n in numbers:
            problem_result *= n

    answer += problem_result

print(answer)
