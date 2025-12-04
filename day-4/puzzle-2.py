from dataclasses import dataclass, field
from enum import Enum
from typing import Sequence


class Directions(Enum):
    N = (-1, 0)
    NE = (-1, -1)
    E = (0, -1)
    SE = (1, -1)
    S = (1, 0)
    SW = (1, 1)
    W = (0, 1)
    NW = (-1, 1)

    def invert(self) -> Directions:
        return {
            Directions.N: Directions.S,
            Directions.NE: Directions.SW,
            Directions.E: Directions.W,
            Directions.SE: Directions.NW,
            Directions.S: Directions.N,
            Directions.SW: Directions.NE,
            Directions.W: Directions.E,
            Directions.NW: Directions.SE,
        }[self]


@dataclass
class Node:

    row: int
    column: int
    roll: bool
    neighbors: dict[Directions, None | Node] = field(default_factory=lambda: dict.fromkeys(Directions, None))

    def tour(self, locations: dict[tuple[int, int], Node], last_row: int, last_column: int) -> None:
        for neighbor in self.neighbors:
            if self.neighbors[neighbor] is None:
                destination_row = self.row + neighbor.value[0]
                destination_column = self.column + neighbor.value[1]
                if destination_row < 0 or destination_row > (last_row + 1) or destination_column < 0 or destination_column > (last_column + 1):
                    continue
                location = locations.get((destination_row, destination_column))
                if location is not None:
                    self.assign(neighbor, location)

    def assign(self, direction: Directions, node: Node) -> None:
        self.neighbors[direction] = node
        node.neighbors[direction.invert()] = self

    @property
    def accessible(self) -> bool:
        adjacent_rolls = sum(v is not None and v.roll for v in self.neighbors.values())
        return self.roll and adjacent_rolls < 4

    def __repr__(self) -> str:
        return f"Node(row={self.row}, column={self.column}, roll={self.roll})"


@dataclass
class Map:

    grid: Sequence[str]
    locations: dict[tuple[int, int], Node] = field(default_factory=dict)
    cleared_rolls: int = 0

    def __post_init__(self):
        self.rows = len(self.grid)
        self.columns = len(self.grid[0])

    def walk(self) -> None:
        for i in range(self.rows):
            for j in range(self.columns):
                new_node = Node(i, j, self.grid[i][j] == "@")
                new_node.tour(self.locations, self.rows, self.columns)
                self.locations[(i, j)] = new_node

    def clear_rolls(self) -> None:
        for location in self.locations.values():
            if location.accessible:
                self.cleared_rolls += 1
                location.roll = False

    def fully_clear(self) -> None:
        while True:
            initial_rolls = self.cleared_rolls
            self.clear_rolls()
            if initial_rolls == self.cleared_rolls:
                break


demo = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".splitlines()

demo_map = Map(demo)
demo_map.walk()
demo_map.fully_clear()
demo_map.cleared_rolls

with open("day-4/roll_grid.txt") as f:
    grid = f.read().splitlines()

puzzle_2 = Map(grid)
puzzle_2.walk()
puzzle_2.fully_clear()
puzzle_2.cleared_rolls
