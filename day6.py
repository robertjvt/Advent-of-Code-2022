import os

with open(os.getcwd() + r"\day6.txt", "r") as file:
    data = file.read()

for i in range(14, len(data)):
    if len(set(data[i-14:i])) == 14:
        print(i)
        break