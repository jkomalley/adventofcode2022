"""Adent of Code Day 11a"""
import re

MONKEYS = []

class Monkey:
    """Class for a monkey holding your items"""
    def __init__(self, id_num, items, operation, op_num, test, true_action, false_action):
        self.num_inspected = 0
        self.id_num = id_num
        self.items = items
        self.operation = operation
        self.op_num = op_num
        self.test = test
        self.true_action = int(true_action)
        self.false_action = int(false_action)

    def __str__(self):
        string = "Monkey " + str(self.id_num) + \
                 ":\nNum inspected: " + \
                 str(self.num_inspected) + \
                 "\nItems: " + \
                 str(self.items) + "\n"
        return string

    def catch_item(self, item: int):
        """adds item to monkey's stash"""
        self.items.append(item)

    def throw_item(self, target_monkey, item: int):
        """throws a given item to a given monkey"""
        MONKEYS[target_monkey].catch_item(item)

    def inspect_items(self):
        """does this monkey's action on all item"""
        oper = self.operation
        num = self.op_num
        # print("Monkey ", self.id_num)
        #go through items, perform our action, run our test, and throw an item
        while len(self.items) > 0:
            item = self.items.pop(0)

            self.num_inspected += 1

            if num == "old":
                cur_num = item
            else:
                cur_num = int(num)
            # print("Old item worry: ", item)
            #perform action
            if oper == "+": # add
                item = item + cur_num
            elif oper == "-": # subtract
                item = item - cur_num
            elif oper == "/": # divide
                item = item / cur_num
            elif oper == "*": # multiply
                item = item * cur_num
            # print("New item worry: ", item)

            item = item % 9699690

            # print("New New item worry: ", item)
            #perform test and throw to monkey based on test
            if item % self.test == 0:
                self.throw_item(self.true_action, item)
            else:
                self.throw_item(self.false_action, item)

        return

def run(rounds):
    """run through monkeys throwing our stuff"""
    for _ in range(0, rounds, 1):
        # print("Round: ", round_num)
        for monkey in MONKEYS:
            monkey.inspect_items()

def main():
    """main function"""

    with open("day11/day11_input.txt", encoding='utf-8') as file:
        input_lines = [line.strip() for line in file.readlines()]

    # read in input and create monkeys
    while len(input_lines) > 0:
        line = input_lines.pop(0)
        if line == '': # blank line, do nothing
            continue
        elif re.match("Monkey [0-9]", line): # new monkey to add to list of monkeys
            id_num = int(line.split(" ")[1].strip(":\n"))
            # print("id num: ", id_num)
            items = input_lines.pop(0)
            items = [int(item) for item in items.strip().split("Starting items: ")[1].split(", ")]
            # print("items: ", items)
            operation = input_lines.pop(0)
            operation = operation.strip().split("Operation: new = old ")[1]
            operation, op_num = operation.split(" ")
            # print("operation: ", operation)
            # print("op num: ", op_num)
            test = input_lines.pop(0)
            test = int(test.strip().split(" ")[-1])
            # print("test: ", test)
            true_action = input_lines.pop(0)
            true_action = true_action.strip().split(" ")[-1]
            # print("true action: ", true_action)
            false_action = input_lines.pop(0)
            false_action = false_action.strip().split(" ")[-1]
            # print("false action: ", false_action)
            cur_monk = Monkey(id_num, items, operation, op_num, test, true_action, false_action)
            MONKEYS.append(cur_monk)

    #begin monkey buisness
    # for monkey in MONKEYS:
    #     print(str(monkey))
    run(10000)
    # for monkey in MONKEYS:
    #     print(str(monkey))

    nums = []
    for monkey in MONKEYS:
        nums.append(monkey.num_inspected)
    nums.sort()

    answer = nums[-1] * nums[-2]

    print("Answer: ", answer)

    return

if __name__=="__main__":
    main()
