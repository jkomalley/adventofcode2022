"""Adevnt of Code 2022 Day 1b"""

with open("day01/day1_input.txt", encoding='utf8') as file:
    lines_s = file.readlines()

cal_counts = []
C = 0
for l in lines_s:
    if l != '\n':
        C += int(l.strip())
    else:
        cal_counts.append(C)
        C = 0

cal_counts.sort()

print(sum(cal_counts[-3:]))
