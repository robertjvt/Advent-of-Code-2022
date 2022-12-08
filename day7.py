import os
import re

with open (os.getcwd() + r"/day7.txt", "r") as file:
    data = file.read().splitlines()

current_dir = ""
dir_data = {}
for command in data:
    if "$ cd" in command:
        req_dir = command.split()[-1]
        if req_dir == "..":
            current_dir = current_dir.split("/")[:-2]
            current_dir = "/".join(current_dir) + "/"
        else:
            if req_dir == "/":
                current_dir = "/"
            else:
                current_dir += req_dir + "/"

    elif "dir " in command:
        if current_dir not in dir_data.keys():
            dir_data[current_dir] = []
        dir_data[current_dir].append(current_dir + command.split()[-1] + "/")

    elif re.search(r"[0-9]+", command):
        size = int(command.split()[0])
        if current_dir not in dir_data.keys():
            dir_data[current_dir] = []
        dir_data[current_dir].append(size)

for k, v in dir_data.items():
    while any(isinstance(item, str) for item in v):
        for i, item in enumerate(v):
            if isinstance(item, str):
                v += dir_data[item]
                v.pop(i)

total = 0
for k, v in dir_data.items():
    value_sum = sum(v)
    if value_sum <= 100000:
        total += value_sum
print(total)

required = 30000000 - (70000000 - sum(dir_data["/"]))
best_size = sum(dir_data["/"])
best_dir = "/"
for k, v in dir_data.items():
    value_sum = sum(v)
    if value_sum >= required and value_sum < best_size:
        best_size = value_sum
        best_dir = k
print(best_dir, best_size)