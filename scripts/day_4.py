def count_accessible(grid):
    h = len(grid)
    w = len(grid[0])

    # offsets for neighbours
    neighbours = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0), 
        (1, 1)
    ]

    accessible = []

    for y in range(h):
        for x in range(w):
            if grid[y][x] != '@':
                continue

            count = 0
            for dy, dx in neighbours:
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w:
                    if grid[ny][nx] == '@':
                        count += 1

            if count < 4:
                accessible.append((x, y))

    return accessible


def main():

    # open file
    with open('data/input_4.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    grid = [list(row) for row in lines]
    result = count_accessible(grid)
    print(len(result))


if __name__ == "__main__":
    main()

