import math
import itertools

with open("day08/input.txt", "r") as f:
    points = [tuple(map(int, line.strip().split(","))) for line in f if line.strip()]

components = {p: frozenset([p]) for p in points}


pairs = list(itertools.combinations(points, 2))
pairs.sort(key=lambda p: math.dist(p[0], p[1]))

part1_ans = 0
part2_ans = 0
all_points_set = set(points)


for i, (p1, p2) in enumerate(pairs):
    if components[p1] != components[p2]:
        new_component = components[p1] | components[p2]

        for p in new_component:
            components[p] = new_component

        if i == 999:
            unique_components = {id(c): c for c in components.values()}.values()
            sizes = sorted([len(c) for c in unique_components], reverse=True)

            if len(sizes) >= 3:
                part1_ans = sizes[0] * sizes[1] * sizes[2]

        if len(new_component) == len(points) and part2_ans == 0:
            part2_ans = p1[0] * p2[0]
            break

print(f"Part 1: {part1_ans}")
print(f"Part 2: {part2_ans}")
