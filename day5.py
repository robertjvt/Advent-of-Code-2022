import os

with open(os.getcwd() + r"\day5.txt", "r") as file:
    stack = [
        ["T", "R", "D", "H", "Q", "N", "P", "B"],
        ["V", "T", "J", "B", "G", "W"],
        ["Q", "M", "V", "S", "D", "H", "R", "N"],
        ["C", "M", "N", "Z", "P"],
        ["B", "Z", "D"],
        ["Z", "W", "C", "V"],
        ["S", "L", "Q", "V", "C", "N", "Z", "G"],
        ["V", "N", "D", "M", "J", "G", "L"],
        ["G", "C", "Z", "F", "M", "P", "T"],
    ]
    orders = []
    for line in file:
        line = line.rstrip().split()
        orders.append([line[1], line[3], line[5]])

for order in orders:
    amount = int(order[0])
    origin = int(order[1]) - 1
    dest = int(order[2]) - 1
    temp = []
    for i in range(amount):
        moving_crate = stack[origin][0]
        stack[origin].pop(0)
        temp.append(moving_crate)

    stack[dest] = temp + stack[dest]

for i in stack:
    print(i[0], end="")

