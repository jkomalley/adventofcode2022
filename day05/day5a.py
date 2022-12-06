"""Advent of code day 5a"""
import re

#     [B]             [B] [S]
#     [M]             [P] [L] [B] [J]
#     [D]     [R]     [V] [D] [Q] [D]
#     [T] [R] [Z]     [H] [H] [G] [C]
#     [P] [W] [J] [B] [J] [F] [J] [S]
# [N] [S] [Z] [V] [M] [N] [Z] [F] [M]
# [W] [Z] [H] [D] [H] [G] [Q] [S] [W]
# [B] [L] [Q] [W] [S] [L] [J] [W] [Z]
#  1   2   3   4   5   6   7   8   9
stacks = [[],
['B', 'W', 'N'],
['L', 'Z', 'S', 'P', 'T', 'D', 'M', 'B'],
['Q', 'H', 'Z', 'W', 'R'],
['W', 'D', 'V', 'J', 'Z', 'R'],
['S', 'H', 'M', 'B'],
['L', 'G', 'N', 'J', 'H', 'V', 'P', 'B'],
['J', 'Q', 'Z', 'F', 'H', 'D', 'L', 'S'],
['W', 'S', 'F', 'J', 'G', 'Q', 'B'],
['Z', 'W', 'M', 'S', 'C', 'D', 'J']]

NUMBERS = "\d+"

def main():
    """Main function"""
    with open("day05/day5_input.txt", encoding='utf8') as file:
        lines = file.readlines()

    for line in lines:
        count, src, dst = [int(i) for i in re.findall(NUMBERS, line)]

        for _ in range(count):
            stacks[dst].append(stacks[src].pop())

    # print(stacks)
    for stack in stacks:
        if len(stack) > 0:
            print(stack.pop(), end="")

    print()

if __name__ == "__main__":
    main()
