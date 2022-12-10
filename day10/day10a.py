"""Advent of Code Day 10a"""
def main():
    """main function"""
    with open("day10/day10_input.txt", encoding='utf-8') as file:
        lines = [line.strip().split(" ") for line in file.readlines()]
    program = []
    for command in lines:
        if command[0] != "noop":
            program.append([command[0], int(command[1])])
        else:
            program.append(command[0])
    cycles = [20,60,100,140,180,220]
    run(program, cycles)

def run(program: list, cycles):
    """run the given program"""
    cycle = 0
    reg_x = 1
    busy = False
    command_num = 0
    cycles_sum = 0
    while True:
        cycle += 1
        if command_num >= len(program):
            break
        if busy is False:
            command = program[command_num]
            command_num += 1
        if cycle in cycles:
            print("Cycle:",cycle,"Command:",command," X:",reg_x)
            cycles_sum += (cycle * reg_x)
        if "noop" in command: #noop
            busy = False
        else: #addx
            if busy is False:
                busy = True
            else:
                busy = False
                reg_x += command[1]
    print("Sum: ", cycles_sum)

if __name__=="__main__":
    main()
