with open("input.txt", "r") as f:
    content = f.read().strip()

parts = content.split("\n\n")

range_lines = parts[0].strip().split("\n")

raw_ranges = []
for line in range_lines:
    if "-" in line:
        start, end = map(int, line.split("-"))
        raw_ranges.append([start, end])

raw_ranges.sort()

merged = []
if raw_ranges:
    current_start, current_end = raw_ranges[0]

    for i in range(1, len(raw_ranges)):
        next_start, next_end = raw_ranges[i]

        if next_start <= current_end:
            current_end = max(current_end, next_end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = next_start, next_end

    merged.append((current_start, current_end))

answer = sum((end - start + 1) for start, end in merged)

print(answer)
