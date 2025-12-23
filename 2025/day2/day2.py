"""
https://adventofcode.com/2025/day/2
"""

answer = 0

with open("input.txt") as f:
    ranges = f.read().split(",")

    for r in ranges:
        if not r:
            continue

        start_str, end_str = r.split("-")
        start, end = int(start_str), int(end_str)

        for num in range(start, end + 1):
            s = str(num)

            if s in (s + s)[1:-1]:
                answer += num

print(answer)
