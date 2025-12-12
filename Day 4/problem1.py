directions = [
    (-1, 0), (1, 0),
    (0, -1), (0, 1),
    (-1, -1), (-1, 1),
    (1, -1), (1, 1)
]

def count_neighbors(grid, r, c):
    rows = len(grid)
    cols = len(grid[r])
    count = 0

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < len(grid[nr]):
            if grid[nr][nc] == '@':
                count += 1

    return count


def simulate_removal(grid):
    rows = len(grid)
    total_removed = 0

    while True:
        to_remove = []

       
        for r in range(rows):
            for c in range(len(grid[r])):
                if grid[r][c] == '@':
                    if count_neighbors(grid, r, c) < 4:
                        to_remove.append((r, c))

       
        if not to_remove:
            break

        
        for r, c in to_remove:
            grid[r][c] = '.'

        total_removed += len(to_remove)

    return total_removed


def main():
    grid =[]

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                grid.append(list(line))

    result = simulate_removal(grid)
    print(result)


if __name__ == "__main__":
    main()
