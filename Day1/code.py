def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    numbers = [int(line.strip()) for line in lines if line.strip()]

    total = sum(numbers)

    print("Total:", total)


if __name__ == "__main__":
    main()
