"""Advent of Code Day 8a"""
forest = []
def main():
    """main function"""
    with open("day08/day8_input.txt", encoding='utf8') as file:
        lines = [l.strip() for l in file.readlines()]

    for line in lines:
        forest.append([int(char) for char in line])

    #count the number of visable trees
    visable_trees = 0
    for row in range(0, len(forest), 1):
        for column in range(0, len(forest[row])):
            if row == 0 or column == 0 or row == (len(forest)-1) or \
                 column == (len(forest[row])-1): #edge tree
                visable_trees += 1
            elif visable(row, column): # tree is visable from outside the forest
                visable_trees += 1
            else:
                visable_trees += 0
    # print(visable(1,1))
    # print_forest()

    print("Visable trees: ", visable_trees)

    return

def visable(tree_y, tree_x):
    """return true if tree at row,col is visable, false otherwise"""
    # north view
    trees = [row[tree_x] for row in forest[:tree_y+1]]
    # print("North view: ", trees)
    # print("Tree: ", tree_y)
    if tallest(trees):
        return True

    # east view
    trees = forest[tree_y][:tree_x+1]
    # print("East view: ", trees)
    # print("Tree: ", tree_x)
    if tallest(trees):
        return True

    # west view
    trees = forest[tree_y][tree_x:]
    trees.reverse()
    # print("West view", trees)
    # print("Tree: ", tree_x)
    if tallest(trees):
        return True

    # south view
    # trees = forest[tree_y][tree_x:]
    trees = [row[tree_x] for row in forest[tree_y:]]
    trees.reverse()
    # print("South view", trees)
    # print("Tree: ", tree_x)
    if tallest(trees):
        return True


    return False

def tallest(trees):
    """return true if last tree is taller than all trees between it and the edge"""
    ret = True
    for i in range(0, len(trees)-1, 1):
        if trees[i] >= trees[-1]:
            ret = False
    # print("Tallest: ", ret)
    return ret

def print_forest():
    """print the forest"""
    for rows in forest:
        for tree in rows:
            print(" ", tree, end="")
        print()

if __name__=="__main__":
    main()
