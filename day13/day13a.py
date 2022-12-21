"""Advent of code day 13a"""

from ast import literal_eval

def compare_pair(pair):
    """compares the given pair and returns true if they are in the correct order, false otherwise
    Compare Rules:
    -> If both values are integers, the lower integer should come first.
       If the left integer is lower than the right integer, the inputs
       are in the right order. If the left integer is higher than the
       right integer, the inputs are not in the right order. Otherwise,
       the inputs are the same integer; continue checking the next part
       of the input.
    -> If both values are lists, compare the first value of each list,
       then the second value, and so on. If the left list runs out of
       items first, the inputs are in the right order. If the right list
       runs out of items first, the inputs are not in the right order.
       If the lists are the same length and no comparison makes a
       decision about the order, continue checking the next part of
       the input.
    -> If exactly one value is an integer, convert the integer to a list
       which contains that integer as its only value, then retry the
       comparison. For example, if comparing [0,0,0] and 2, convert the
       right value to [2] (a list containing 2); the result is then
       found by instead comparing [0,0,0] and [2].
    """
    left = pair[0]
    right = pair[1]

    #check if both values are ints, if yes, compare them
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    #check if both values are lists, if so, compare them
    elif isinstance(left, list) and isinstance(right, list):
        i = 0
        while i < len(left) and i < len(right):
            val = compare_pair([left[i], right[i]])
            if val == -1:
                return -1
            elif val == 1:
                return 1
            i += 1
        if i == len(left) and i < len(right):
            return -1
        elif i < len(left) and i == len(right):
            return 1
        else:
            return 0
    #check if only one value is an int, if so make it a list and compare them
    else:
        if isinstance(left, int):
            list_list = [left]
            list_right = right
        else:
            list_list = left
            list_right = [right]
        return compare_pair([list_list, list_right])


    return None

def main():
    """main function"""
    with open("day13/day13_input.txt", encoding='utf-8') as file:
        lines = file.read()

    pairs_string = lines.split("\n\n")

    pairs = []

    for pair_string in pairs_string:
        first_string, second_string = pair_string.split("\n")
        # print("First: ", first_string)
        # print("Second: ", second_string)

        first_pair = literal_eval(first_string)#make_list(first_string)
        second_pair = literal_eval(second_string)#make_list(second_string)

        pairs.append([first_pair, second_pair])
    index = 0
    count = 0
    for pair in pairs:
        index += 1
        if compare_pair(pair) == -1:
            count += index

    print("Answer: ", count)

    return

if __name__=="__main__":
    main()
