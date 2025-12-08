from dataclasses import dataclass
from math import prod, sqrt
from typing import NamedTuple


class Coordinates(NamedTuple):
    x: int
    y: int
    z: int


def straight_line_distance(coordinate_1: Coordinates, coordinate_2: Coordinates) -> float:
    squared_differences = ((c1 - c2) ** 2 for c1, c2 in zip(coordinate_1, coordinate_2))
    sum_squares = sum(squared_differences)
    return sqrt(sum_squares)


@dataclass
class BoxPair:
    distance: float
    box_1: Coordinates
    box_2: Coordinates

    def __eq__(self, other):
        if not hasattr(other, "distance"):
            raise TypeError("Cannont compare these objects!")
        return self.distance == other.distance

    def __gt__(self, other):
        if not hasattr(other, "distance"):
            raise TypeError("Cannont compare these objects!")
        return self.distance > other.distance

    def __ge__(self, other):
        if not hasattr(other, "distance"):
            raise TypeError("Cannont compare these objects!")
        return self.distance >= other.distance

    def __lt__(self, other):
        if not hasattr(other, "distance"):
            raise TypeError("Cannont compare these objects!")
        return self.distance < other.distance

    def __le__(self, other):
        if not hasattr(other, "distance"):
            raise TypeError("Cannont compare these objects!")
        return self.distance <= other.distance

demo = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

with open("day-8/input.txt") as f:
    raw_boxes = f.read()

junction_boxes = []
for line in raw_boxes.splitlines():
    int_list = [int(num) for num in line.split(",")]
    junction_boxes.append(Coordinates(*int_list))

distances = []
for i in range(len(junction_boxes)):
    for j in range(i + 1, len(junction_boxes)):
        distance = straight_line_distance(junction_boxes[i], junction_boxes[j])
        distances.append(BoxPair(distance, junction_boxes[i], junction_boxes[j]))

circuits = []
for pair in sorted(distances)[:1000]:
    added = False
    for circuit in circuits:
        if pair.box_1 in circuit or pair.box_2 in circuit:
            circuit.add(pair.box_1)
            circuit.add(pair.box_2)
            added = True
            break
    if not added:
        circuits.append({pair.box_1, pair.box_2})

joined = True
while joined:
    joined = False
    for i in range(len(circuits)):
        for j in range(i + 1, len(circuits)):
            if circuits[i].intersection(circuits[j]):
                circuits[i] |= circuits[j]
                circuits[j] = set()
                joined = True

prod(len(c) for c in sorted(circuits, key=len, reverse=True)[:3])
