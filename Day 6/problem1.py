def main():

    with open("input.txt", "r") as f:
        lines = [line.rstrip("\n") for line in f]

    if not lines:
        print(0)
        return

    height = len(lines)
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
       
        op_char = None
        for ch in lines[-1][start:end]:
            if ch != " ":
                op_char = ch
                break
        if op_char not in ("+", "*"):
            raise ValueError(f"No operator found in block columns {start}-{end}")

       
        operands = []
        for col in range(end - 1, start - 1, -1):  
            
            digits = []
            for r in range(0, height - 1):  
                ch = lines[r][col]
                if ch != " ":
                    digits.append(ch)
            if digits:
                num_str = "".join(digits)  
                
                if not num_str.isdigit():
                    raise ValueError(f"Non-digit characters found in column {col}: {num_str!r}")
                operands.append(int(num_str))

      
        if op_char == "+":
            result = sum(operands)
        else:
            prod = 1
            for v in operands:
                prod *= v
            result = prod

        total_sum += result

    print(total_sum)


if __name__ == "__main__":
    main()
