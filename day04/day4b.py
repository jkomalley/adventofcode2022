"""Advent of Code Day 4b"""
def main():
    """main function"""
    with open("day04/day4_input.txt", encoding='utf8') as file:
        lines = file.readlines()

    num_overlapped = 0

    for line in lines:
        range1, range2 = line.strip().split(",")

        range1 = [int(i) for i in range1.split("-")]
        range2 = [int(i) for i in range2.split("-")]

        set1 = set_range(range1)
        set2 = set_range(range2)
        # print(set1, set2)
        if len(set1.intersection(set2)) != 0:
            num_overlapped += 1
            # print("overlapped")

    print("Num overlapped: ", num_overlapped)

def set_range(r):
    """returns a list containing every number within the given range"""
    return set([i for i in range(r[0], r[1]+1)])

if __name__ == "__main__":
    main()
