from dataclasses import dataclass

@dataclass
class FreshID:
    """Linked list of ID ranges"""

    start: int
    stop: int

    @classmethod
    def from_string(cls, raw_range: str, splitter: str = "-") -> FreshID:
        start, stop = raw_range.split(splitter)
        return cls(int(start), int(stop))

    def overlap(self, other: FreshID) -> bool:
        a = self if self.start <= other.start else other
        b = self if self is not a else other
        return a.stop >= b.start

    def combine(self, other: FreshID) -> FreshID:
        start = min(self.start, other.start)
        stop = max(self.stop, other.stop)
        return FreshID(start, stop)

    @property
    def range(self) -> int:
        return 1 + (self.stop - self.start)


def recursive_combine(ids: list[FreshID]) -> list[FreshID]:
    mask = [True for _ in ids]
    for i in range(len(ids) - 1):
        if ids[i].overlap(ids[i + 1]):
            ids[i + 1] = ids[i + 1].combine(ids[i])
            mask[i] = False
    out = [ids[i] for i in range(len(ids)) if mask[i]]
    return out if all(mask) else recursive_combine(out)


with open("day-5/input.txt") as f:
    puzzle_ids = f.read().splitlines()

fresh_ids = []
for row in puzzle_ids:
    if row == "":
        break
    fresh_ids.append(FreshID.from_string(row))

fresh_ids.sort(key=lambda id: id.start)

sum(ids.range for ids in recursive_combine(fresh_ids))
