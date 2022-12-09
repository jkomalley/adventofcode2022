"""Advent of Code Day 9a"""
import math

#      [x,y]
head = [0,0]
tail = [0,0]

grid = [[0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]]

def main():
    """main function"""
    with open("day09/day9_small_input.txt", encoding='utf-8') as file:
        moves = [line.strip().split(" ") for line in file.readlines()]

    moves = [[move[0], int(move[1])] for move in moves]

    for move in moves:
        while move[1] != 0:
            if move[0] == 'U': #up
                head[0] += 1
            elif move[0] == 'L': #left
                head[1] -= 1
            elif move[0] == 'D': #down
                head[0] -= 1
            elif move[0] == 'R': #right
                head[1] += 1
            move[1] -= 1

            update_tail()

            print_grid()

    return

def update_tail():
    """update location of tail"""
    dis = distance(head, tail)

    if dis > 1:
        if

def distance(point_a, point_b):
    """ret distance between point_a and point_b"""
    x_part = point_b[0] - point_a[0]
    x_part_squared = x_part * x_part
    y_part = point_b[1] - point_a[1]
    y_part_squared = y_part * y_part
    return math.sqrt(x_part_squared + y_part_squared)

def print_grid():
    """print grid"""
    grid[head[0]][head[1]] = 1
    print("-"*100)
    grid.reverse()
    for row in grid:
        # row.reverse()
        for point in row:
            print(" ", point, end='')
        print()
        # row.reverse()
    grid.reverse()
    print("-"*100)
    grid[head[0]][head[1]] = 0

if __name__=="__main__":
    main()
