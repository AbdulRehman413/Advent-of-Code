def check(num_str, k):
    drop = len(num_str) - k
    stack = []

    for digit in num_str:
        while drop and stack and stack[-1] < digit:
            stack.pop()
            drop -= 1
        stack.append(digit)

    return ''.join(stack[:k])


def main():
    stackk = []   

    with open("input.txt", "r") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue

            max12 = check(s, 12)
            stackk.append(int(max12))   


    print(sum(stackk))


if __name__ == "__main__":
    main()
