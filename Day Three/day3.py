
DAY_THREE_INPUT = "Day Three/Puzzle Input/day3.txt"

def parse_battery_banks():
    joltages = []
    with open (DAY_THREE_INPUT) as battery_banks:
        for bank in battery_banks:
            bank = bank.strip()
            joltages.append(find_joltage(bank))
    return joltages

def find_joltage(bank):
    size = len(bank) - 1
    fast = size - 1
    largest_seen, largest_pair = int(bank[size]), 0

    while fast >= 0:
        current_pair = str(bank[fast]) + str(largest_seen)
        largest_pair = max(largest_pair, int(current_pair))

        if int(bank[fast]) > largest_seen:
            largest_seen = int(bank[fast])
        fast -= 1
    return largest_pair

if __name__ == "__main__":
    joltages = parse_battery_banks()
    print(sum(joltages))