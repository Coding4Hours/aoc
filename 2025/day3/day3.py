total_output_joltage = 0

with open("input.txt") as f:
    for line in f:
        bank = line.strip()
        if not bank:
            continue

        target_length = 12
        k = len(bank) - target_length
        stack = []

        for digit in bank:
            while k > 0 and stack and stack[-1] < digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        max_joltage_str = "".join(stack[:target_length])
        total_output_joltage += int(max_joltage_str)

print(f"total output joltage: {total_output_joltage}")
