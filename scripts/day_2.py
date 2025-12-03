def is_invalid_id(num_str):
    
    length = len(num_str)
    half_length = length // 2
    if num_str[:half_length] == num_str[half_length:]:
        return True
    else:
        return False


def main():

    with open('data/input_2.txt') as f:
        line = f.read().strip()

    # split by commas
    parts = [p for p in line.split(',') if p]

    # get number ranges
    ranges = []
    for part in parts:
        start_str, end_str = part.split('-')

        # generate range between start and end (inclusive)
        start = int(start_str)
        end = int(end_str)
        this_range = []
        for num in range(start, end + 1):
            num_str = str(num)
            this_range.append(num_str)
        ranges.append(this_range)


    invalid_ids = []
    for r in ranges:
        for num_str in r:
            if is_invalid_id(num_str):
                invalid_ids.append(num_str)
    print(f'Found {len(invalid_ids)} invalid IDs:')

    total_sum = 0
    for invalid_id in invalid_ids:
        total_sum += int(invalid_id)

    print(f'Sum of all invalid IDs: {total_sum}')

if __name__ == "__main__":
    main()

