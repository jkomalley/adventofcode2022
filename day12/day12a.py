"""Advent of code day 12a"""

def find_path(start_location, end_location, grid):
    """find a path from the start to the finish"""

    visited_blocks = []
    blocks_queue = []
    #               0:up   1:right 2:down   3:left
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    visited_blocks.append(start_location)
    blocks_queue.append([start_location, grid[start_location[0]][start_location[1]]])

    while blocks_queue:
        cur_block = blocks_queue.pop(0)

        if cur_block[0] == end_location:
            print("Found end!")
            print(cur_block)
            print(len(cur_block[1]) - 1)
            return

        for neighbor in directions:
            cur_x = cur_block[0][1] + neighbor[1]
            cur_y = cur_block[0][0] + neighbor[0]
            if cur_y >= 0 and cur_y < len(grid) and cur_x >= 0 and cur_x < len(grid[cur_y]):
                if ord(cur_block[1][-1]) - ord(grid[cur_y][cur_x]) >= -1:
                    neighbor_block = [cur_y, cur_x]
                    if neighbor_block not in visited_blocks:
                        visited_blocks.append(neighbor_block)
                        blocks_queue.append([neighbor_block, cur_block[1] + grid[cur_y][cur_x]])

def main():
    """main function"""
    grid = []

    with open("day12/day12_input.txt", encoding='utf-8') as file:
        lines = file.readlines()

    cur_line = -1
    for line in lines:
        cur_line += 1
        grid.append([])
        line = line.strip()
        for char in line:
            grid[cur_line].append(char)

    #get start and end points
    start = []
    end = []
    for y_index in range(0, len(grid), 1):
        for x_index in range(0, len(grid[y_index])):
            if grid[y_index][x_index] == 'S':
                start = [y_index, x_index]
                grid[y_index][x_index] = 'a'
            if grid[y_index][x_index] == 'E':
                end = [y_index, x_index]
                grid[y_index][x_index] = 'z'

    find_path(start, end, grid)

if __name__=="__main__":
    main()
