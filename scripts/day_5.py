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

if __name__ == "__main__":
    main()

