with open("input.txt", "r") as f:
    grid = [list(line.strip()) for line in f if line.strip()]

rows = len(grid)
cols = len(grid[0])
total_removed = 0

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

while True:
    to_remove = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                neighbor_count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == "@":
                            neighbor_count += 1

                if neighbor_count < 4:
                    to_remove.append((r, c))

    if not to_remove:
        break

    total_removed += len(to_remove)
    for r, c in to_remove:
        grid[r][c] = "."

print(f"removed: {total_removed}")
