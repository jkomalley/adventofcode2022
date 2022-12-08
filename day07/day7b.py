"""Advent of Code Day 7a"""
import re
import sys
def main():
    """main function"""
    with open("day07/day7_input.txt", encoding='utf8') as file:
        lines = [l.strip() for l in file.readlines()]
    cur_dir = []
    directories = {}

    #calculate each dir's size
    for line in lines:
        if re.match(r"\$ cd \.\.", line): # go up a dir match
            prev_dir_s = list_to_str(cur_dir)
            cur_dir.pop()
            cur_dir_s = list_to_str(cur_dir)
            directories[cur_dir_s] = directories.get(cur_dir_s) + directories.get(prev_dir_s)
        elif re.match(r"\$ cd ([/]|[a-zA-Z]+)", line): # go into a dir match
            cur_dir.append(line.split(" ")[2])
            cur_dir_s = list_to_str(cur_dir)
            if cur_dir_s not in directories:
                directories[cur_dir_s] = 0
        elif re.match(r"\$ ls", line): # list dir match
            continue
        elif re.match(r"dir [a-zA-Z]+[.]?[a-zA-Z]*", line): # dir listing match
            continue
        elif re.match(r"([\d]+) [a-zA-Z]+[.]?[a-zA-Z]*", line): # file listing match
            size = int(line.split(" ")[0].strip())
            cur_dir_s = list_to_str(cur_dir)
            if cur_dir_s in directories:
                directories[cur_dir_s] = directories.get(cur_dir_s) + size

        # print(directories)

    #if cur_dir isnt the base dir, do "cd .." until it is to add sub dir sizes to parent dirs
    while len(cur_dir) != 1:
        prev_dir_s = list_to_str(cur_dir)
        cur_dir.pop()
        cur_dir_s = list_to_str(cur_dir)
        directories[cur_dir_s] = directories.get(cur_dir_s) + directories.get(prev_dir_s)

    # find how much more space is needed to update
    used_space = directories.get("/")
    update_space = 30000000
    total_space = 70000000
    available_space = total_space - used_space
    needed_space = update_space - available_space

    # find the smallest dir with enough space for the update
    answer = sys.maxsize
    for size in directories.values():
        if size >= needed_space and size < answer:
            answer = size

    print("Answer: ", answer)

def list_to_str(dir_list):
    """convert dir list to str"""
    return "/".join(map(str, dir_list))

if __name__ == "__main__":
    main()
