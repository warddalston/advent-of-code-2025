import re
from collections import defaultdict

equations = defaultdict(list)

with open("day-6/input.txt") as f:
    for line in f.readlines():
        formatted_line = re.sub("\\s+", " ", line).strip().split(" ")
        for i, char in enumerate(formatted_line):
            equations[i].append(char)

sum(eval(equation[-1].join(equation[:-1])) for equation in equations.values())
