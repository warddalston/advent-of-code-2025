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
    graph[key] = value.split(" ")

to_search = deque()
to_search.append("you")
paths = 0
while to_search:
    current = to_search.popleft()
    for destination in graph[current]:
        if destination == "out":
            paths += 1
            continue
        to_search.append(destination)

paths
