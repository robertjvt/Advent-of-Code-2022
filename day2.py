import os

with open(os.getcwd() + r"\day2.txt", "r") as file:
    data = [line.split() for line in file.read().splitlines()]

scores = {"A": 1, "B": 2, "C": 3}
win = {"A": "B", "B": "C", "C": "A"}
lose = {"A": "C", "B": "A", "C": "B"}

score = 0
for item in data:
    if item[1] == "Y":
        score += 3
        score += scores[item[0]]
    elif item[1] == "Z":
        score += 6
        score += scores[win[item[0]]]
    else:
        score += scores[lose[item[0]]]

print(score)

