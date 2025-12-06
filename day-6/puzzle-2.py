from collections import defaultdict

equations = defaultdict(list)

with open("day-6/input.txt") as f:
    for line in f.readlines():
        for i, char in enumerate(line):
            equations[i].append(char)

running_total = 0
current_values = []

for row in equations.values():
    last_char = row[-1]
    if last_char == "+" or last_char == "*":
        operation = last_char
    if all((char == " ") or (char == "\n") for char in row):  # need the line break for the last row!
        running_total += eval(operation.join(current_values))
        current_values = []
    else:
        current_values.append("".join(char for char in row[:-1] if char != " "))

running_total
