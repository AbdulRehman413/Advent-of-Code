def main():
   
    with open("input.txt", "r") as f:
        lines = [line.rstrip("\n") for line in f]

    height =len(lines)
    width = max(len(line) for line in lines)

    
    lines = [line.ljust(width) for line in lines]

    
    problem_cols = []
    inside = False

    for col in range(width):
        column_is_space = all(lines[r][col] == " " for r in range(height))

        if not column_is_space and not inside:
           
            start = col
            inside = True

        if column_is_space and inside:
            
            end = col
            inside = False
            problem_cols.append((start, end))

    
    if inside:
        problem_cols.append((start, width))

    total_sum = 0

    for start, end in problem_cols:
        
        operator_column = lines[-1][start:end]
        operator = next(ch for ch in operator_column if ch != " ")

      
        numbers = []
        for r in range(height - 1):
            slice = lines[r][start:end].strip()
            if slice != "":
                numbers.append(int(slice))

        
        if operator == "+":
            result = sum(numbers)
        else:
            result = 1
            for x in numbers:
                result *= x

        total_sum += result

    print(total_sum)


if __name__ == "__main__":
    main()
