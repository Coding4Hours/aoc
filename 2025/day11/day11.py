graph = {}
with open("input.txt", "r") as f:
    for line in f:
        if ":" not in line:
            continue
        name, neighbors = line.split(":")
        graph[name.strip()] = neighbors.strip().split()

memo = {}


def count_paths(start, end):
    if start == end:
        return 1
    if start not in graph:
        return 0
    state = (start, end)
    if state in memo:
        return memo[state]

    total = 0
    for neighbor in graph[start]:
        total += count_paths(neighbor, end)

    memo[state] = total
    return total


tew = count_paths("svr", "dac") * count_paths("dac", "fft") * count_paths("fft", "out")

wun = count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out")

answer = tew + wun

print(answer)
