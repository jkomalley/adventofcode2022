"""Advent of Code Day 4a"""
def main():
    """main function"""
    with open("day04/day4_input.txt", encoding='utf8') as file:
        lines = file.readlines()

    num_fully_contained = 0

    for line in lines:
        range1, range2 = line.strip().split(",")

        range1 = [int(i) for i in range1.split("-")]
        range2 = [int(i) for i in range2.split("-")]

        # print(range1, range2)
        if range1[0] <= range2[0] and range1[1] >= range2[1] or \
         range1[0] >= range2[0] and range1[1] <= range2[1]:
            num_fully_contained += 1
            # print("contained")
    
    print("Num fully contained: ", num_fully_contained)

if __name__ == "__main__":
    main()
