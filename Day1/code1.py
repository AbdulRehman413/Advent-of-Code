def main():
    with open("input1.txt", "r") as f:
        data = f.readlines()

    s = 50
    total = 0
    for  line in data:
        line = line.strip()
        k = int(line[1:])
        dir = line[0]
        full = k//100
        r = k%100
        if dir == "R":
            if r > 0 and s + r >= 100:
                extra = 1
            else:
                extra = 0
            total += full + extra
            s = (s + r) % 100
        if dir == "L":
            if r > 0 and s - r < 0:
                extra = 1
            else:
                extra = 0
            total += full + extra
            s = (s - r) % 100

    print(total)



if __name__ == "__main__":
    main()