import os


def move(x, y, knots):
    knots[0][0] += x
    knots[0][1] += y

    for i in range(1, 10):
        hx, hy = knots[i-1]
        tx, ty = knots[i]

        x, y = hx-tx, hy-ty
        dx, dy = abs(x), abs(y)
        if dx + dy > 2: # diagonal
            if x < 0:
                knots[i][0] -= 1
            else:
                knots[i][0] += 1
            
            if y < 0:
                knots[i][1] -= 1
            else:
                knots[i][1] += 1

        elif dx > 1 and dy == 0: # horizontal
            if x < 0:
                knots[i][0] -= 1
            else:
                knots[i][0] += 1

        elif dx == 0 and dy > 1: # vertical
            if y < 0:
                knots[i][1] -= 1
            else:
                knots[i][1] += 1
    return knots


def main():
    with open(os.getcwd() + r"\day9.txt", "r") as file:
        data = []
        for line in file:
            line = line.rstrip().split()
            data.append([line[0], int(line[1])])

    dir_dict = {
        "R": [1, 0],
        "L": [-1, 0],
        "U": [0, 1],
        "D": [0,-1]
    }

    knots = []
    for _ in range(10):
        knots.append([0, 0])

    tail = []

    for line in data:
        direction, amount = line[0], line[1]
        x, y = dir_dict[direction]
        for _ in range(amount):
            knots = move(x, y, knots)
            if str(knots[-1]) not in tail: # should change to set()
                tail.append(str(knots[-1]))

    print(len(tail))        


if __name__ == "__main__":
    main()