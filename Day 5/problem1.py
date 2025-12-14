def main():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

   
    blank_index = lines.index("")
    range_lines = lines[:blank_index]

    
    ranges = []
    for rl in range_lines:
        a, b = rl.split("-")
        ranges.append((int(a), int(b)))

   
    ranges.sort()

    
    merged = []
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end + 1:
            
            current_end = max(current_end, end)
        else:
            
            merged.append((current_start, current_end))
            current_start, current_end = start, end

   
    merged.append((current_start, current_end))

    
    total = 0
    for a, b in merged:
        total += (b - a + 1)

    print(total)


if __name__ == "__main__":
    main()
