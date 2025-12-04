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
                s = str(k)

                if len(s) % 2 != 0:
                    continue

                mid = len(s)//2
                first = s[:mid]
                second = s[mid:]


                if first == second:
                    stack.append(int(s))
                        

    print(sum(stack))
                        
                        
if __name__ == "__main__":
    main()
