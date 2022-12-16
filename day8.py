import os
import math


def check_for_less(input_list, value):
    return(all(x < value for x in input_list))


def check_view(to_check, v):
    score = 0
    for value in to_check:
        if value >= v:
            return score + 1
        score += 1
    return score


def main():
    trees = {}
    with open (os.getcwd() + r"/day8.txt", "r") as file:
        coords = [0, 0]
        for line in file:
            for digit in line.rstrip():
                trees[tuple(coords)] = int(digit)
                coords[1] += 1
            coords[1] = 0
            coords[0] += 1

    max_x, max_y = max(trees.items())[0][0], max(trees.items())[0][1]
    total_trees = 0
    viewing_distances = []

    for k, v in trees.items():
        x, y = k[0], k[1]
        if x != 0 and y != 0 and x != max_x and y != max_y: # check if tree is visible
            to_check = [[], [], [], []]
            
            for i in range(1, y+1):
                to_check[0].append(trees[(x, y-i)])
            
            for i in range(1, max_y-y+1):
                to_check[1].append(trees[(x, y+i)])

            for i in range(1, x+1):
                to_check[2].append(trees[(x-i, y)])
            
            for i in range(1, max_x-x+1):
                to_check[3].append(trees[(x+i, y)])
            
            view = [0, 0, 0, 0]
            view[0], view[1], view[2], view[3] = check_view(to_check[0], v), check_view(to_check[1], v), check_view(to_check[2], v), check_view(to_check[3], v)

            viewing_distances.append(math.prod(view))
        else: # tree is on outside and therefore visible
            total_trees += 1
    
    print(total_trees)
    print(max(viewing_distances))


if __name__ == "__main__":
    main()
    