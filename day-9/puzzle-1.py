demo = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

with open("day-9/input.txt") as f:
    puzzle = f.read()

grid = []
x_values = []
y_values = []

for coordinate_pair in puzzle.splitlines():
    x, y = coordinate_pair.split(",")
    x_values.append(int(x))
    y_values.append(int(y))
    grid.append([(int(x), int(y)), 1])

x_sorted = sorted(location[0][0] for location in grid)
y_sorted = sorted(location[0][1] for location in grid)
x_min, x_max = x_sorted[0], x_sorted[-1]
y_min, y_max = y_sorted[0], y_sorted[-1]


def area(grid_point_1: list[int], grid_point_2: list[int]) -> int:
    horizontal = 1 + abs(grid_point_1[0] - grid_point_2[0])
    vertical = 1 + abs(grid_point_1[1] - grid_point_2[1])
    return horizontal * vertical


def find_max(
    grid_point: list[int],
    x_min: int = x_min,
    x_max: int = x_max,
    y_min: int = y_min,
    y_max: int = y_max,
) -> int:
    top_left = area(grid_point, [x_min, y_min])
    top_right = area(grid_point, [x_min, y_max])
    bottom_left = area(grid_point, [x_max, y_min])
    bottom_right = area(grid_point, [x_max, y_max])
    return max([top_left, top_right, bottom_left, bottom_right])

for location in grid:
    location[1] = find_max(location[0])

grid = sorted(grid, key=lambda x: x[1], reverse=True)
max_i, i, out = len(grid), 0, 1
while i < max_i - 1:
    location, max_possible_for_location = grid[i]
    for j in range(i + 1, max_i):
        alternative, max_possible_for_alternative = grid[j]
        if out > max_possible_for_alternative:
            max_i = j
            break
        new_area = area(location, alternative)
        if new_area > out:
            out = new_area
    i += 1
