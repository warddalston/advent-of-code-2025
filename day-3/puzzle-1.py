demo_banks = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]

demo_targets = [98, 89, 78, 92]
demo_sum = 357

# we want to turn on TWO batteries that form the largest possible two-digit number
# therefore, anything witha 9 in the 10's is better than anything with an 8 and so on

def max_joltage(bank: str) -> int:
    first_battery, second_battery = bank[0], bank[1]
    for i in range(1, len(bank) - 1):
        if bank[i] > first_battery:
            first_battery, second_battery = bank[i], bank[i + 1]
            continue
        if bank[i] > second_battery:
            second_battery = bank[i]
    if bank[-1] > second_battery:
        second_battery = bank[-1]

    return int(first_battery + second_battery)

with open("day-3/battery_banks.txt") as raw_input:
    banks = raw_input.read().split("\n")[:-1]

sum(max_joltage(bank) for bank in banks)
