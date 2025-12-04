def is_repeating_pattern(num):
    s = str(num)
    n = len(s)

    
    for p in range(1, n):
        if n % p != 0:
            continue  

        pattern = s[:p]
        if pattern * (n // p) == s:
            return True

    return False


def main():
    with open ("input.txt", "r") as f:
        data = f.readlines()

    
    stack = []
   

    for i in data:
        i = i.strip()
        
        ranges = i.split(",")

        for r in ranges:
            start , end = map(int, r.split("-"))

            for k in range(start, end+1):
                if is_repeating_pattern(k):
                    stack.append(k)
                        

    print(sum(stack))
                        
                        
if __name__ == "__main__":
    main()

