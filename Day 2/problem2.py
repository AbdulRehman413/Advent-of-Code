def ch(n):
    s= str(n)
    d =len(s)

    
    for z in range(1,d):
        if d %z!= 0:
            continue  

        p =s[:z]

        if p*(d// z) == s:
            return True
        
    return False


def main():
    with open("input.txt", "r")as f:
        data = f.readlines()


    stack = []
   
    for i in data:
        i = i.strip()
        ranges = i.split(",")
        for r in ranges:
                st,e = map(int,r.split("-"))
                for k in range(st, e+1):
                    if ch(k):
                        stack.append(k)
                            

    print(sum(stack))
                        
                        
if __name__ == "__main__":
    main()

