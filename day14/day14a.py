"""Advent of code day 14a"""
import sys

def print_wall(wall, y_range = [i for i in range(0, 11, 1)],\
                x_range = [i for i in range(490, 510, 1)]):
    """prints the wall"""
    y_index = 0
    x_index = 0
    for row in wall:
        if y_index in y_range:
            for space in row:
                if x_index in x_range:
                    print(space, end="")
                x_index += 1
        if y_index in y_range:
            print()
        y_index += 1
        x_index = 0

def sand_fall(wall):
    """simulate sand falling"""
    sand_start = [0,500]
    round_num = 0
    while True:
        cur_sand = sand_start[::]
        while True:
            wall[cur_sand[0]][cur_sand[1]] = 'o'
            if cur_sand[0] + 1 >= len(wall): # reached end
                print("Answer: ", round_num)
                sys.exit()
            elif wall[cur_sand[0]+1][cur_sand[1]] == '.': #check below
                # print_wall(wall)
                wall[cur_sand[0]][cur_sand[1]] = '.'
                cur_sand[0] += 1
            elif wall[cur_sand[0]+1][cur_sand[1]-1] == '.': #check down left
                # print_wall(wall)
                wall[cur_sand[0]][cur_sand[1]] = '.'
                cur_sand[0] += 1
                cur_sand[1] -= 1
            elif wall[cur_sand[0]+1][cur_sand[1]+1] == '.': #check down right
                # print_wall(wall)
                wall[cur_sand[0]][cur_sand[1]] = '.'
                cur_sand[0] += 1
                cur_sand[1] += 1
            else:
                break
        round_num += 1

def main():
    """main function"""
    with open("day14/day14_input.txt", encoding='utf-8') as file:
        lines = file.readlines()

    wall = []

    for _ in range(500):
        wall.append(['.' for _ in range(600)])

    rocks = []
    for line in lines:
        points = line.strip().split(' -> ')
        points = [[int(index) for index in point.split(',')] for point in points]
        rocks.append(points)

    for rock in rocks:
        first_point = rock.pop(0)
        second_point = rock.pop(0)
        while True:
            inc_y = 1
            if first_point[1] > second_point[1]:
                inc_y = -1

            inc_x = 1
            if first_point[0] > second_point[0]:
                inc_x = -1

            for y_index in range(first_point[1], second_point[1]+inc_y, inc_y):
                for x_index in range(first_point[0], second_point[0]+inc_x, inc_x):
                    wall[y_index][x_index] = '#'
            first_point = second_point
            if len(rock) > 0:
                second_point = rock.pop(0)
            else:
                break

    sand_fall(wall)

if __name__=="__main__":
    main()
