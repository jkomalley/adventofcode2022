"""Adevnt of Code 2022 Day 1a"""

with open("day1/day1_input.txt", encoding='utf8') as file:
    lines_s = file.readlines()

cal_counts = []
cur_cal_count = 0
for l in lines_s:
    if l != '\n':
        cur_cal_count += int(l.strip())
    else:
        cal_counts.append(cur_cal_count)
        cur_cal_count = 0

cal_counts.sort()

print(cal_counts[-1])
