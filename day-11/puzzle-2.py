from collections import defaultdict, deque


demo = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""

with open("day-11/input.txt") as f:
    puzzle = f.read()

graph = {}
for line in puzzle.splitlines():
    key, value = line.split(': ')
    graph[key] = set(value.split(" "))

def reachable_in_x(start: str, graph=graph):
    reachable_places = defaultdict(set)
    stepper = {start}
    still_going = True
    i = 0
    while still_going:
        still_going = False
        for node in stepper:
            if node != "out":
                for next_step in graph[node]:
                    still_going = True
                    reachable_places[i].add(next_step)
        if still_going:
            stepper = reachable_places[i]
            i += 1
    return reachable_places

nested_dict = {k: reachable_in_x(k) for k in graph}

can_reach_fft = set()
for k, v in nested_dict.items():
    for kk, vv in v.items():
        if "fft" in vv:
            can_reach_fft.add(k)

to_search = deque()
to_search.append(["svr"])
paths_a = 0
searched = 0

while to_search:

    if searched % 1000 == 0 and searched > 0:
        print(f"Percent searched: {searched / (searched + len(to_search))}")

    history = to_search.popleft()
    current_node = history[-1]
    for destination in graph[current_node]:
        new_history = [*history, destination]
        if destination == "fft":
             paths_a += 1
        elif destination in history:
            print("Already been there!")
            continue
        elif destination in {'out', 'dac', 'svr'}:
            print("bad path!")
            continue
        elif destination not in can_reach_fft:
            continue
        else:
            to_search.append(new_history)
    searched += 1

paths_a

can_reach_fft = set()
for k, v in nested_dict.items():
    for kk, vv in v.items():
        if "dac" in vv:
            can_reach_fft.add(k)

to_search = deque()
to_search.append(["fft"])
paths_b = 0
searched = 0

while to_search:

    if searched % 1000 == 0 and searched > 0:
        print(f"Percent searched: {searched / (searched + len(to_search))}")

    history = to_search.popleft()
    current_node = history[-1]
    for destination in graph[current_node]:
        new_history = [*history, destination]
        if destination == "dac":
             paths_b += 1
        elif destination in history:
            print("Already been there!")
            continue
        elif destination in {'out', 'fft', 'svr'}:
            print("bad path!")
            continue
        elif destination not in can_reach_fft:
            continue
        else:
            to_search.append(new_history)
    searched += 1

paths_b

can_reach_fft = set()
for k, v in nested_dict.items():
    for kk, vv in v.items():
        if "out" in vv:
            can_reach_fft.add(k)

to_search = deque()
to_search.append(["dac"])
paths_c = 0
searched = 0

while to_search:

    if searched % 1000 == 0 and searched > 0:
        print(f"Percent searched: {searched / (searched + len(to_search))}")

    history = to_search.popleft()
    current_node = history[-1]
    for destination in graph[current_node]:
        new_history = [*history, destination]
        if destination == "out":
             paths_c += 1
        elif destination in history:
            print("Already been there!")
            continue
        elif destination in {'dac', 'fft', 'svr'}:
            print("bad path!")
            continue
        elif destination not in can_reach_fft:
            continue
        else:
            to_search.append(new_history)
    searched += 1

paths_c

paths_a * paths_b * paths_c
