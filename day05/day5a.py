"""Advent of code day 5a"""
def main():
    """Main function"""
    with open("day05/day5_input.txt", encoding='utf8') as file:
        lines = file.readlines()

    start_arrangement = ""

    line = lines.pop()

    while not line.startswith("move"):
        start_arrangement = start_arrangement + line
        line = lines.pop()

    print(start_arrangement)

if __name__ == "__main__":
    main()
