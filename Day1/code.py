
def main():
    with open ("input.txt", "r") as f:
        data = f.readlines()
        



    dial = 50
    counter = 0
    for i in data:
        i = i.strip()
        number = int(i[1:])
        if i.startswith("L"):
            dial = (dial - number) % 100

            
        elif i.startswith("R"):
            dial = (dial + number) % 100


        if dial == 0:
            counter += 1
            

    print(counter)



if __name__ == "__main__":
    main()

