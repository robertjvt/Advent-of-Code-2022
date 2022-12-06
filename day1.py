import os

with open(os.getcwd() + r"\day1.txt", "r") as file:
    data = file.read().splitlines()
    data.append("")

total, elves = 0, {}
for i, line in enumerate(data):
    if line == "":
        i += 1
        elves[i] = total
        total = 0
    else:
        total += int(line)

print(max(elves.values()))
print(sum(sorted(elves.values())[-3:]))
