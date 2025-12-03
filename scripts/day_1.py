START_POSITION = 50

def main():
    with open('data/input_1.txt', 'r') as file:
        lines = file.readlines()
    lines = [line.strip('\n') for line in lines]

    directions, movements = [line[0] for line in lines], [int(line[1:]) for line in lines]

    position = START_POSITION
    count_at_zero = 0

    # modulo 100 to simulate circular path
    for i, (direction, movement) in enumerate(zip(directions, movements)):
        # print(position)
        # print(direction, movement)
        if direction == 'L':
            position = (position - movement) % 100
        elif direction == 'R':
            position = (position + movement) % 100
        else:
            raise ValueError(f'Invalid direction: {direction} at line {i+1}')
        # print(f'New position: {position}\n')

        # count how many times position is zero *ater* movement
        if position == 0:
            count_at_zero += 1

    print(f'Final position: {position}')
    print(f'Count at zero: {count_at_zero}')


if __name__ == "__main__":
    main()

