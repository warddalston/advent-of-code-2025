from collections import defaultdict
from typing import NamedTuple


class Tile(NamedTuple):
    x: int
    y: int


def area(grid_point_1: Tile, grid_point_2: Tile) -> int:
    horizontal = 1 + abs(grid_point_1[0] - grid_point_2[0])
    vertical = 1 + abs(grid_point_1[1] - grid_point_2[1])
    return horizontal * vertical


with open("day-9/input.txt") as f:
    puzzle = f.read()


grid = []
for coordinate_pair in puzzle.splitlines():
    x, y = map(int, coordinate_pair.split(","))
    grid.append(Tile(y, x))

green_tiles = []
for i in range(len(grid)):
    next_i = i + 1 if i != len(grid) - 1 else 0
    horizontal = grid[i].y == grid[next_i].y
    if horizontal:
        increasing = grid[i].x < grid[next_i].x
        if increasing:
            step_range = range(grid[i].x + 1, grid[next_i].x)
        else:
            step_range = range(grid[i].x - 1, grid[next_i].x, -1)
        green_tiles.extend([Tile(j, grid[i].y) for j in step_range])
    else:
        increasing = grid[i].y < grid[next_i].y
        if increasing:
            step_range = range(grid[i].y + 1, grid[next_i].y)
        else:
            step_range = range(grid[i].y - 1, grid[next_i].y, -1)
        green_tiles.extend([Tile(grid[i].x, j) for j in step_range])


y_lookup = defaultdict(set)
x_lookup = defaultdict(set)
for tile in grid:
    y_lookup[tile.y].add(tile.x)
    x_lookup[tile.x].add(tile.y)

for tile in green_tiles:
    y_lookup[tile.y].add(tile.x)
    x_lookup[tile.x].add(tile.y)

x_min_lookup = {x: min(y_set) for x, y_set in x_lookup.items()}
x_max_lookup = {x: max(y_set) for x, y_set in x_lookup.items()}

y_min_lookup = {y: min(x_set) for y, x_set in y_lookup.items()}
y_max_lookup = {y: max(x_set) for y, x_set in y_lookup.items()}

def is_outside(tile: Tile) -> bool:
    # look up
    if tile.y > x_max_lookup[tile.x]:
        return True

    # look down
    if tile.y < x_min_lookup[tile.x]:
        return True

    # look right
    if tile.x < y_min_lookup[tile.y]:
        return True

    # look left
    if tile.x > y_max_lookup[tile.y]:
        return True

    return False


def is_outside_rectangle(tile_1: Tile, tile_2: Tile) -> bool:
    top_y = max(tile_1.y, tile_2.y)
    bottom_y = min(tile_1.y, tile_2.y)
    right_x = max(tile_1.x, tile_2.x)
    left_x = min(tile_1.x, tile_2.x)

    top_left = Tile(left_x, top_y)
    top_right = Tile(right_x, top_y)
    bottom_left = Tile(left_x, bottom_y)
    bottom_right = Tile(right_x, bottom_y)

    return any(map(is_outside, [top_left, top_right, bottom_left, bottom_right]))

LEFT_LIMIT = 48563
RIGHT_LIMIT = 50218
current_max = 1

for i in range(len(grid)):
    for j in range(i + 1, len(grid)):
        tile_1 = grid[i]
        tile_2 = grid[j]

        single_side = (tile_1.x <= LEFT_LIMIT and tile_2.x <= LEFT_LIMIT) or (tile_1.x >= RIGHT_LIMIT and tile_2.x >= RIGHT_LIMIT)
        is_valid = not is_outside_rectangle(tile_1, tile_2)

        if single_side and is_valid:
            new_area = area(tile_1, tile_2)
            current_max = max(current_max, new_area)

print(current_max)
