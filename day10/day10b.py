"""Advent of Code Day 10b"""
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
    run(program)

def run(program: list):
    """run the given program"""
    cycle = 0
    reg_x = 1
    busy = False
    command_num = 0
    while True:
        cycle += 1
        if command_num >= len(program):
            break
        if busy is False:
            command = program[command_num]
            command_num += 1
        draw(cycle,reg_x)
        if "noop" in command: #noop
            busy = False
        else: #addx
            if busy is False:
                busy = True
            else:
                busy = False
                reg_x += command[1]
    print()

def draw(cycle, reg_x):
    """draw pixel"""
    cycle = (cycle - 1) % 40
    if cycle == 0:
        print()
    if cycle in range(reg_x-1,reg_x+2,1):
        print('#', end='')
    else:
        print('.', end='')

if __name__=="__main__":
    main()
