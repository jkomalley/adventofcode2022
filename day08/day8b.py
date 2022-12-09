"""Advent of Code Day 8a"""
forest = []
def main():
    """main function"""
    with open("day08/day8_input.txt", encoding='utf8') as file:
        lines = [l.strip() for l in file.readlines()]

    for line in lines:
        forest.append([int(char) for char in line])

    #count the number of visable trees
    highest_score = 0
    cur_score = 0
    for row in range(0, len(forest), 1):
        for column in range(0, len(forest[row])):
            cur_score = calc_visability_score(row, column)
            if cur_score > highest_score:
                highest_score = cur_score

    print("Highest score: ", highest_score)

    # print("score: ", calc_visability_score(3, 2))

    return

def calc_visability_score(tree_y, tree_x):
    """calculates the vis. score of a given tree in the forest"""
    scores = {"north": 0, "south": 0, "east": 0, "west": 0}

    #north score
    trees = [row[tree_x] for row in forest[:tree_y]]
    trees.reverse()
    # print("North view: ", trees)
    for tree in trees:
        scores["north"] = scores.get("north") + 1
        if tree >= forest[tree_y][tree_x]:
            break

    #south score
    trees = [row[tree_x] for row in forest[tree_y+1:]]
    # trees.reverse()
    # print("South view: ", trees)
    for tree in trees:
        scores["south"] = scores.get("south") + 1
        if tree >= forest[tree_y][tree_x]:
            break

    #east score
    trees = forest[tree_y][:tree_x]
    trees.reverse()
    # print("East view: ", trees)
    for tree in trees:
        scores["east"] = scores.get("east") + 1
        if tree >= forest[tree_y][tree_x]:
            break

    #west score
    trees = forest[tree_y][tree_x+1:]
    # trees.reverse()
    # print("West view: ", trees)
    for tree in trees:
        scores["west"] = scores.get("west") + 1
        if tree >= forest[tree_y][tree_x]:
            break

    # print(scores)
    score = 1
    for val in scores.values():
        score *= val
    return score

if __name__=="__main__":
    main()
