# Another fucking graph problem

from collections import deque


demo = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

with open("day-11/input.txt") as f:
    puzzle = f.read()

graph = {}
for line in puzzle.splitlines():
    key, value = line.split(': ')
    graph[key] = [value.split(" "), 0]

to_search = deque()
to_search.append("you")
paths = 0
while to_search:
    current = to_search.popleft()
    for destination in graph[current][0]:
        if destination == "out":
            paths += 1
            continue
        graph[destination][1] += 1
        to_search.append(destination)

paths
