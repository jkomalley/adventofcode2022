"""Advent of Code Day 9a"""
import math

#      [x,y]
# head = [0,0]
# tail = [0,0]
NUM_KNOTS = 9
knots = [[0,0],# Head
         [0,0],# 1
         [0,0],# 2
         [0,0],# 3
         [0,0],# 4
         [0,0],# 5
         [0,0],# 6
         [0,0],# 7
         [0,0],# 8
         [0,0]]# 9 (tail)

def main():
    """main function"""
    with open("day09/day9_input.txt", encoding='utf-8') as file:
        moves = [line.strip().split(" ") for line in file.readlines()]

    moves = [[move[0], int(move[1])] for move in moves]

    tail_locations = []

    for move in moves:
        # print(knots)
        while move[1] != 0:
            if move[0] == 'U': #up
                knots[0][0] += 1
            elif move[0] == 'L': #left
                knots[0][1] -= 1
            elif move[0] == 'D': #down
                knots[0][0] -= 1
            elif move[0] == 'R': #right
                knots[0][1] += 1
            move[1] -= 1

            update_knots()

            tail_locations.append(" ".join(str(val) for val in knots[-1]))

    num_visited = len(set(tail_locations))

    print("Num tail visited: ", num_visited)

    return

def update_knots():
    """update all knots on the rope"""
    for i in range(1, len(knots), 1):
        head = knots[i-1]
        tail = knots[i]
        dis = distance(head, tail)
        # print("distance: ", dis)
        if dis > 1:
            # x move
            if tail[0] < head[0]:
                tail[0] = tail[0] + 1
            elif tail[0] > head[0]:
                tail[0] = tail[0] - 1
            # y move
            if tail[1] < head[1]:
                tail[1] = tail[1] + 1
            elif tail[1] > head[1]:
                tail[1] = tail[1] - 1

def distance(point_a, point_b):
    """ret floor of distance between point_a and point_b"""
    x_part = point_b[0] - point_a[0]
    x_part_squared = x_part * x_part
    y_part = point_b[1] - point_a[1]
    y_part_squared = y_part * y_part
    return math.floor(math.sqrt(x_part_squared + y_part_squared))

if __name__=="__main__":
    main()
