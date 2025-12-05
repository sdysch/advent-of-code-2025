def main():

    # open file
    with open('data/input_3.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    total = 0
    for line in lines:
        best = 0

        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                pair = (line[i], line[j])
                val = int(''.join(map(str, pair)))

                if val > best:
                    best = val

        total += best

    print(total)


if __name__ == "__main__":
    main()

