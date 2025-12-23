with open("input.txt") as f:
    input_data = f.read()


lines = input_data.strip().split("\n")
points = []
for line in lines:
    if not line.strip():
        continue
    x, y = map(int, line.strip().split(","))
    points.append((x, y))

n = len(points)

h_edges = []
v_edges = []

for i in range(n):
    p1 = points[i]
    p2 = points[(i + 1) % n]
    if p1[1] == p2[1]:
        h_edges.append((p1[1], min(p1[0], p2[0]), max(p1[0], p2[0])))
    else:
        v_edges.append((p1[0], min(p1[1], p2[1]), max(p1[1], p2[1])))

max_area = 0

for i in range(n):
    for j in range(i + 1, n):
        p1 = points[i]
        p2 = points[j]

        x1, y1 = p1
        x2, y2 = p2

        width = abs(x1 - x2) + 1
        height = abs(y1 - y2) + 1
        area = width * height

        if area <= max_area:
            continue

        xmin, xmax = min(x1, x2), max(x1, x2)
        ymin, ymax = min(y1, y2), max(y1, y2)

        is_valid = True

        for h, a, b in h_edges:
            if ymin < h < ymax:
                if max(xmin, a) < min(xmax, b):
                    is_valid = False
                    break
        if not is_valid:
            continue

        for v, a, b in v_edges:
            if xmin < v < xmax:
                if max(ymin, a) < min(ymax, b):
                    is_valid = False
                    break
        if not is_valid:
            continue

        cx = (xmin + xmax) / 2.0
        cy = (ymin + ymax) / 2.0

        on_boundary = False
        for h, a, b in h_edges:
            if abs(cy - h) < 1e-9:
                if a <= cx <= b:
                    on_boundary = True
                    break
        if not on_boundary:
            for v, a, b in v_edges:
                if abs(cx - v) < 1e-9:
                    if a <= cy <= b:
                        on_boundary = True
                        break

        if on_boundary:
            max_area = area
            continue

        cy_test = cy + 1e-5

        intersections = 0
        for v, a, b in v_edges:
            if v > cx:
                if a <= cy_test <= b:
                    intersections += 1

        if intersections % 2 == 1:
            max_area = area

print(max_area)
