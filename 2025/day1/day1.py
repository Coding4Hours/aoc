"""
https://adventofcode.com/2025/day/1
"""

abs_dial = 50
zero_counter = 0
method_counter = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        val = int(line[1:])

        old_dial = abs_dial

        if direction == "L":
            abs_dial -= val

            crossings = ((old_dial - 1) // 100) - ((abs_dial - 1) // 100)
            method_counter += crossings

        elif direction == "R":
            abs_dial += val

            crossings = (abs_dial // 100) - (old_dial // 100)
            method_counter += crossings

        if abs_dial % 100 == 0:
            zero_counter += 1

print(f"password: {zero_counter}")
print(f"password with method 0x434C49434B: {method_counter}")
