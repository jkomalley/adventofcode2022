""" Adevnt of Code 2022 Day 2a """
def main():
    """ main function """
    with open("day2/day2_input.txt", encoding='utf8') as file:
        lines = file.readlines()

    my_score = 0
    for line in lines:
        oponent_choice, my_choice = line.strip().split(" ")

        # oponent_choice = convert_to_num(oponent_choice)
        # my_choice = convert_to_num(my_choice)
        print("Input: [my_choice: ", my_choice, " opponent_choice: ", oponent_choice, "]")
        # check who won and tally points
        if oponent_choice == "A" and my_choice == "X": # their Rock vs. my Rock: draw
            my_score = my_score + 3 + convert_to_num(my_choice)
        elif oponent_choice == "A" and my_choice == "Y": # their Rock vs. my Paper: win
            my_score = my_score + 6 + convert_to_num(my_choice)
        elif oponent_choice == "A" and my_choice == "Z": # their Rock vs. my Scissors: lose
            my_score = my_score + 0 + convert_to_num(my_choice)
        elif oponent_choice == "B" and my_choice == "X": # their Paper vs. my Rock: lose
            my_score = my_score + 0 + convert_to_num(my_choice)
        elif oponent_choice == "B" and my_choice == "Y": # their Paper vs. my Paper: draw
            my_score = my_score + 3 + convert_to_num(my_choice)
        elif oponent_choice == "B" and my_choice == "Z": # their Paper vs. my Scissors: win
            my_score = my_score + 6 + convert_to_num(my_choice)
        elif oponent_choice == "C" and my_choice == "X": # their Scissors vs. my Rock: win
            my_score = my_score + 6 + convert_to_num(my_choice)
        elif oponent_choice == "C" and my_choice == "Y": # their Scissors vs. my Paper: lose
            my_score = my_score + 0 + convert_to_num(my_choice)
        elif oponent_choice == "C" and my_choice == "Z": # their Scissors vs. my Scissors: draw
            my_score = my_score + 3 + convert_to_num(my_choice)
        else:
            print("ERROR: Bad input")

    print("My score: ", my_score)

def convert_to_num(choice):
    """Converts a rps choice to a number representation"""
    ret = 0
    if choice == "X" or choice == "A": #rock
        ret = 1
    elif choice == "Y" or choice == "B": #paper
        ret = 2
    elif choice == "Z" or choice == "C": #scissors
        ret = 3

    return ret

if __name__ == "__main__":
    main()
