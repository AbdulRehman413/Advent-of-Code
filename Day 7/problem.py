def count_splits_from_file(filename="input.txt"):
 
    with open(filename, "r") as f:
        lines = [line.rstrip("\n") for line in f]

    if not lines:
        return 0

    rows =len(lines)
    cols = max(len(line) for line in lines)
   
    grid = [list(line.ljust(cols)) for line in lines]

    start = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                start = (r, c)
                break
        if start:
            break
    if not start:
        raise ValueError("No S found in input")

   
    beams = {start}
    splits = 0

    while beams:
        next_beams = set()
        for (r, c) in beams:
            nr = r + 1
            nc = c
            if nr >= rows:
                
                continue

            cell = grid[nr][nc]

            if cell == '.':
                
                next_beams.add((nr, nc))
            elif cell == '^':
                
                splits += 1
                
                left = (nr, nc - 1)
                right = (nr, nc + 1)
                if 0 <= left[1] < cols:
                    next_beams.add(left)
                if 0 <= right[1] < cols:
                    next_beams.add(right)
            else:
    
                continue

        beams = next_beams

    return splits


if __name__ == "__main__":
    result = count_splits_from_file("input.txt")
    print(result)
