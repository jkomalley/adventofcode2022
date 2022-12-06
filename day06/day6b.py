"""Advent of Code day 6a"""
def main():
    """main function"""
    with open("day06/day6_input.txt", encoding='utf8') as file:
        datastream = file.readline()

    for i in range(0, len(datastream)-1):
        if len(set(datastream[i:i+14])) == 14:
            print(i+14)
            break

if __name__ == "__main__":
    main()
