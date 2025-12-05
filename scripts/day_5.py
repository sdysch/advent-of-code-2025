def main():

    # open files
    with open('data/input_5_id_ranges.txt') as f:
        id_ranges = f.readlines()
        id_ranges = [line.strip() for line in id_ranges]

    with open('data/input_5_ids.txt') as f:
        ids = f.readlines()
        ids = [line.strip() for line in ids]


    # generate start and ends of all valid ids
    valid_id_ranges = []
    for id_range in id_ranges:
        start, end = id_range.split('-')
        valid_id_ranges.append((int(start), int(end)))

    # check which ids are valid
    valid_ids = []
    for id_ in ids:
        id_int = int(id_)
        for start, end in valid_id_ranges:
            if start <= id_int <= end:
                valid_ids.append(id_)
                break

    print(len(valid_ids))

    # part 2

    # first check which ranges are overlapping and merge them
    merged_ranges = []
    valid_id_ranges.sort()
    current_start, current_end = valid_id_ranges[0]
    for start, end in valid_id_ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            merged_ranges.append((current_start, current_end))
            current_start, current_end = start, end


    # find number of valid ids
    num_valid = sum(end - start + 1 for start, end in merged_ranges)
    print(num_valid)


if __name__ == "__main__":
    main()

