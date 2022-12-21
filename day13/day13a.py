"""Advent of code day 13a"""

def print_pairs(pairs):
    """print the given pairs"""
    print("Pairs:")
    for pair in pairs:
        print(pair[0])
        print(pair[1])
        print()

def make_list(string):
    """make list form string"""
    parent_lists = []
    cur_list = []
    for cur_char in string[1:]:
        if cur_char == "[":
            parent_lists.append(cur_list)
            cur_list = []
        elif cur_char == "]":
            if len(parent_lists) == 0:
                return cur_list
            else:
                temp_list = parent_lists.pop()
                temp_list.append(cur_list)
                cur_list = temp_list
        elif cur_char == ",":
            continue
        else:
            cur_list.append(cur_char)

    return None

def main():
    """main function"""
    with open("day13/day13_small_input.txt", encoding='utf-8') as file:
        lines = file.read()

    pairs_string = lines.split("\n\n")

    pairs = []

    for pair_string in pairs_string:
        first_string, second_string = pair_string.split("\n")
        # print("First: ", first_string)
        # print("Second: ", second_string)

        first_pair = make_list(first_string)
        second_pair = make_list(second_string)

        pairs.append([first_pair, second_pair])

    print_pairs(pairs)

    return

if __name__=="__main__":
    main()
