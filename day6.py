import os

with open(os.getcwd() + r"\day6.txt", "r") as file:
    data = file.read()

for i in range(len(data)):
    if i < 14:
        continue
    if len(set(data[i-14:i])) == 14:
        print(i)
        break