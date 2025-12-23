import re


lines = open("input.txt").read().strip().split("\n")[30:]

count = 0
for line in lines:
    numbers = [int(n) for n in re.findall(r"\d+", line)]

    if len(numbers) >= 2:
        first_val = numbers[0]
        second_val = numbers[1]
        remaining_sum = sum(numbers[2:])

        if 9 * remaining_sum <= first_val * second_val:
            count += 1

print("Day 12:", count)
