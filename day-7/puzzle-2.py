from dataclasses import dataclass

@dataclass
class QuantumTachyon:
    position: tuple[int, int]
    indirect_exits: int = 0

    splitters = {}

    @staticmethod
    def step_left(position: tuple[int, int]) -> tuple[int, int]:
        """Step down and to the left."""
        return (position[0] + 1, position[1] - 1)

    @staticmethod
    def step_down(position: tuple[int, int]) -> tuple[int, int]:
        """Step down."""
        return (position[0] + 1, position[1])

    @staticmethod
    def step_right(position: tuple[int, int]) -> tuple[int, int]:
        """Step down and to the right."""
        return (position[0] + 1, position[1] + 1)

    @staticmethod
    def check_manifold(position: tuple[int, int]) -> bool:
        """Check if a location in the manifold is a splitter."""
        return manifold[position[0]][position[1]] == "^"

    def _grow(self, step_direction: str) -> int:
        """Recursively explore the tree and count the number of exits."""
        stepper = self.step_left if step_direction == "left" else self.step_right
        position = stepper(self.position)

        while position[0] < len(manifold):
            if self.check_manifold(position, ):
                if position not in self.splitters:
                    self.splitters[position] = QuantumTachyon(position)
                    self.splitters[position].indirect_exits = self.splitters[position].grow()
                return self.splitters[position].indirect_exits
            else:
                position = self.step_down(position)
        return 1

    def grow(self) -> int:
        """Explore the tree and count the number of exits."""
        return self._grow("left") + self._grow("right")


demo = (
""".......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
).splitlines()[2:][0::2]

with open("day-7/input.txt") as f:
    manifold = f.read().splitlines()[2:][0::2]

for i, char in enumerate(manifold[0]):
    if char == "^":
        tree = QuantumTachyon(position=(0, i))
        QuantumTachyon.splitters[(0, i)] = tree
        print(tree.grow())
        break

