from functools import cache

demo_banks = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]


@cache
def largest_sub_number(digit: str, target_len: int = 12) -> str:

    # Base cases
    if len(digit) == 1:
        return digit
    if len(digit) == 2:
        return max(digit[0], digit[1])

    # figure out which of the first two to keep
    if digit[0] < digit[1]:
        out= digit[1:]
    else:
        out = digit[0] + largest_sub_number(digit[1:])

    # Keep going until we are at the desired size
    if len(out) > target_len:
        out = largest_sub_number(out)
    return out


sum(int(largest_sub_number(bank)) for bank in demo_banks)

with open("day-3/battery_banks.txt") as raw_input:
    banks = raw_input.read().split("\n")[:-1]

sum(int(largest_sub_number(bank)) for bank in banks)
