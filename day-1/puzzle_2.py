position = 50
position_zero = 0


def parse_rotation(raw: str) -> int:
    direction = -1 if raw[0] == "L" else 1
    amount = raw[1:-1]
    return int(amount) * direction


with open("day-1/input-puzzle-1.txt") as puzzle_1_input:
    for raw_rotation in puzzle_1_input.readlines():
        rotation = parse_rotation(raw_rotation)
        new_position = position + rotation

        for p in range(position, new_position, 1 if rotation > 0 else -1):
            position_zero += ((p % 100) == 0)

        position = new_position

print(position_zero)
