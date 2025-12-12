directions = [
    (-1, 0), (1, 0),      # top, bottom
    (0, -1), (0, 1),      # left, right
    (-1, -1), (-1, 1),    # top-left, top-right
    (1, -1), (1, 1)       # bottom-left, bottom-right
]

def count_accessible_rolls(grid):
    rows = len(grid)
    ans = 0

    for r in range(rows):
        cols = len(grid[r])
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            at_neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < len(grid[nr]):
                    if grid[nr][nc] == '@':
                        at_neighbors += 1

            # Only accessible if fewer than 4 neighbors
            if at_neighbors < 4:
                ans += 1

    return ans

def main():
    grid = []

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                grid.append(list(line))

    result = count_accessible_rolls(grid)
    print(result)

if __name__ == "__main__":
    main()
