"""Advent of Code Day 4a"""
def main():
    """main function"""
    with open("day04/day4_input.txt", encoding='utf8') as file:
        lines = file.readlines()

    for line in lines:
        range1, range2 = line.split(",")
        print(range1, " ", range2)

if __name__ == "__main__":
    main()
