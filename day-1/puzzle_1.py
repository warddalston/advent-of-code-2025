position = 50
position_zero = 0

def parse_rotation(raw: str) -> int:
    direction = -1 if raw[0] == "L" else 1
    amount = raw[1:-1]
    return int(amount) * direction


with open("day-1/input-puzzle-1.txt") as puzzle_1_input:
    for rotation in puzzle_1_input.readlines():
        position  += parse_rotation(rotation)
        if (position % 100) == 0:
            position_zero += 1

print(position_zero)
