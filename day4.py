import os
import re

with open(os.getcwd() + r"\day4.txt", "r") as file:
    data = []
    for line in file:
        line = re.split(',|-', line.rstrip())
        data.append([list(range(int(line[0]), int(line[1])+1)), list(range(int(line[2]), int(line[3])+1))])

total = 0
for pair in data:
    if set(pair[0]).intersection(set(pair[1])):
        total += 1

print(total)
