import os 

with open(os.getcwd() + r"\day3.txt", "r") as file:
    data = file.read().splitlines()
    paired_data = [data[i-2:i+1] for i in range(len(data)) if i % 3 == 2]

priority = {}
letters = "abcdefghijklmnopqrstuvwxyz"
upperletters = letters.upper()

for i, (letter, upperletter) in enumerate(zip(letters, upperletters)):
    priority[letter] = 1 + i
    priority[upperletter] = 27 + i

total = 0
for one, two, three in paired_data:
    checked = []
    for letter in one:
        if letter in two and letter in three and letter not in checked:
            checked.append(letter)
            total += priority[letter]

print(total)