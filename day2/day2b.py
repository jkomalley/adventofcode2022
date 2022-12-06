""" Adevnt of Code 2022 Day 2a """
ROCK = "A"
PAPER = "B"
SCISSORS = "C"

def main():
    """ main function """
    with open("day2/day2_input.txt", encoding='utf8') as file:
        lines = file.readlines()

    my_score = 0
    for line in lines:
        oponent_choice, win_lose_draw = line.strip().split(" ")

        # oponent_choice = convert_to_num(oponent_choice)
        # my_choice = convert_to_num(my_choice)
        print("Input: [win_lose_draw: ", win_lose_draw, " opponent_choice: ", oponent_choice, "]")
        # check who won and tally points
        if oponent_choice == "A" and win_lose_draw == "X": # their Rock, I need to lose, my choice Scissors
            my_score = my_score + 0 + convert_to_num(SCISSORS)
        elif oponent_choice == "A" and win_lose_draw == "Y": # their Rock, I need to draw, my choice Rock
            my_score = my_score + 3 + convert_to_num(ROCK)
        elif oponent_choice == "A" and win_lose_draw == "Z": # their Rock, I need to win, my choice Paper
            my_score = my_score + 6 + convert_to_num(PAPER)
        elif oponent_choice == "B" and win_lose_draw == "X": # their Paper, I need to lose, my choice Rock
            my_score = my_score + 0 + convert_to_num(ROCK)
        elif oponent_choice == "B" and win_lose_draw == "Y": # their Paper, I need to draw, my choice Paper
            my_score = my_score + 3 + convert_to_num(PAPER)
        elif oponent_choice == "B" and win_lose_draw == "Z": # their Paper, I need to win, my choice Scissors
            my_score = my_score + 6 + convert_to_num(SCISSORS)
        elif oponent_choice == "C" and win_lose_draw == "X": # their Scissors, I need to lose, my choice Paper
            my_score = my_score + 0 + convert_to_num(PAPER)
        elif oponent_choice == "C" and win_lose_draw == "Y": # their Scissors, I need to draw, my choice Scissors
            my_score = my_score + 3 + convert_to_num(SCISSORS)
        elif oponent_choice == "C" and win_lose_draw == "Z": # their Scissors, I need to win, my choice Rock
            my_score = my_score + 6 + convert_to_num(ROCK)
        else:
            print("ERROR: Bad input")

    print("My score: ", my_score)

def convert_to_num(choice):
    """Converts a rps choice to a number representation"""
    ret = 0
    if choice == "A": #rock
        ret = 1
    elif choice == "B": #paper
        ret = 2
    elif choice == "C": #scissors
        ret = 3

    return ret

if __name__ == "__main__":
    main()
