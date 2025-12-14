def main():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    
    blank_index = lines.index("")   # find blank line

    range_lines = lines[:blank_index]
    id_lines = lines[blank_index + 1:]

    ranges = []
    for rl in range_lines:
        a, b = rl.split("-")
        ranges.append((int(a), int(b)))

    ingredient_ids = [int(x) for x in id_lines]

    fresh_count = 0

    # Check each ID
    for id_num in ingredient_ids:
        for a, b in ranges:
            if a <= id_num <= b:
                fresh_count += 1
                break   # no need to check other ranges

    print(fresh_count)


if __name__ == "__main__":
    main()
