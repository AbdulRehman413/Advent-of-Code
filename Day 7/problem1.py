def count_timelines_from_file(filename="input.txt"):
   
    with open(filename, "r") as f:
        lines = [line.rstrip("\n") for line in f]

    if not lines:
        return 0

    rows =len(lines)
    cols = max(len(l) for l in lines)
    grid = [list(l.ljust(cols)) for l in lines]

    
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

    
    current = {start: 1}
    finished = 0  

    while current:
        nxt = {}
        for (r, c), cnt in current.items():
            nr = r + 1
            nc = c
            
            if nr >= rows:
                finished += cnt
                continue

            cell = grid[nr][nc]
            if cell == "." or cell == "S":
               
                nxt[(nr, nc)] = nxt.get((nr, nc), 0) + cnt
            elif cell == "^":
                
                left_col = nc - 1
                right_col = nc + 1

                
                if left_col < 0 or left_col >= cols:
                    finished += cnt
                else:
                    nxt[(nr, left_col)] = nxt.get((nr, left_col), 0) + cnt

                
                if right_col < 0 or right_col >= cols:
                    finished += cnt
                else:
                    nxt[(nr, right_col)] = nxt.get((nr, right_col), 0) + cnt
            else:
                
                finished += cnt

        current = nxt

    return finished


if __name__ == "__main__":
    ans = count_timelines_from_file("input.txt")
    print(ans)
