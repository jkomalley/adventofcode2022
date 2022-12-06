""" Adevnt of Code 2022 Day 3a """
def main():
    """main function"""
    priority_sum = 0

    with open("day03/day3_input.txt", encoding='utf8') as file:
        lines = file.readlines()
    # find common items between compartments and add up priorities
    for line in lines:
        first_compartment, second_compartment = line[:len(line)//2], line[len(line)//2:]

        common_letter = list(set(first_compartment) & set(second_compartment))[0]

        # print("Common letter: ", common_letter, " Priority: ", letter_to_num(common_letter))

        priority_sum += letter_to_num(common_letter)

    print("priority_sum: ", priority_sum)

def letter_to_num(letter):
    """convert letter to number priority"""
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96

if __name__ == "__main__":
    main()
