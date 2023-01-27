"""Advent of code day 15a"""
import re

SENSOR_X = 0
SENSOR_Y = 1
BEACON_X = 2
BEACON_Y = 3
DISTANCE = 4

def get_distance(pair):
    """returns distance between two points"""
    distance = abs(pair[SENSOR_X] - pair[BEACON_X]) + abs(pair[SENSOR_Y] - pair[BEACON_Y])
    return distance

def main():
    """main function"""
    with open("day15/day15_input.txt", encoding='utf-8') as file:
        lines = file.readlines()

    sensor_beacon_pairs = []

    min_x = 0
    max_x = 0 # max x axis value

    for line in lines:
        cur_pair = [int(num) for num in re.findall(r'-?\d+', line)]

        dis = get_distance(cur_pair)
        cur_pair.append(dis)

        if cur_pair[SENSOR_X] > max_x:
            max_x = cur_pair[SENSOR_X] + cur_pair[DISTANCE]
        if cur_pair[BEACON_X] > max_x:
            max_x = cur_pair[BEACON_X]
        if cur_pair[SENSOR_X] < min_x:
            min_x = cur_pair[SENSOR_X] - cur_pair[DISTANCE]
        if cur_pair[BEACON_X] < min_x:
            min_x = cur_pair[BEACON_X]
        sensor_beacon_pairs.append(cur_pair)

    # print(sensor_beacon_pairs)

    target_line = 2000000 # y axis constant

    # for each spot on target line, go through each sensor + distance to see
    # if the sensor is in range of the target line AND if it's beacon is NOT
    # in the current spot.
    spots = set()
    for cur_x in range(min_x, max_x + 1, 1):
        current_spot = [cur_x, target_line]
        for pair in sensor_beacon_pairs:
            if get_distance([cur_x, target_line, pair[SENSOR_X], pair[SENSOR_Y]]) <= pair[DISTANCE] and\
                not (cur_x == pair[BEACON_X] and target_line == pair[BEACON_Y]):
                # print(cur_x)
                spots.add(str(current_spot))

    print("Answer: ", len(spots))

if __name__=="__main__":
    main()
