import bisect
from typing import NamedTuple


class FreshID(NamedTuple):
    start: int
    stop: int
    id: str

    def is_fresh(self, ingredient_id: int) -> bool:
        return (ingredient_id >= self.start) & (ingredient_id <= self.stop)


def start_key(id: FreshID):
    return id.start


def stop_key(id: FreshID):
    return id.stop


demo_ids = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
""".splitlines()

with open("day-5/input.txt") as f:
    puzzle_ids = f.read().splitlines()

fresh_ids, available_ids ,add_ids = [], [], True

for row in puzzle_ids:
    if "" == row:
        add_ids = False
        continue
    if add_ids:
        start, stop = row.split('-')
        fresh_ids.append(FreshID(int(start), int(stop), row))
    else:
        available_ids.append(int(row))

start_sorted = sorted(fresh_ids, key=start_key)
stop_sorted = sorted(fresh_ids, key=stop_key)

available_ingredient_count = 0
for available_id in available_ids:

    largest_starter = bisect.bisect_right(start_sorted, available_id, key=start_key)
    possible_starters = {fresh_id.id for fresh_id in start_sorted[:largest_starter]}

    smallest_stopper = bisect.bisect_left(stop_sorted, available_id, key=stop_key)
    possible_stoppers = {fresh_id.id for fresh_id in stop_sorted[smallest_stopper:]}

    if possible_starters & possible_stoppers:
        available_ingredient_count += 1

available_ingredient_count
