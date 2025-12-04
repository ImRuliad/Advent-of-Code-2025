DAY_TWO_INPUT = "Day Two/Puzzle Input/day2.txt"

def parse_ids():
    with open(DAY_TWO_INPUT) as file:
        for line in file:
            line = line.strip()
            parsed_ids = line.split(",")
    return parsed_ids

def get_ranges(parsed_ids):
    ranges = []
    for id in parsed_ids:
        bounds = id.split("-")
        lower_bound, upper_bound = int(bounds[0]), int(bounds[1])
        
        for number in range(lower_bound, upper_bound + 1):
            if len(str(number)) % 2 == 0:
                ranges.append(number)
    return ranges

def find_invalid_ids(ranges):
    sum_of_invalids = 0
    for number in ranges:
        number = str(number)
        mid = len(str(number)) // 2
        if number[:mid] == number[mid:]:
            sum_of_invalids += int(number)
    return sum_of_invalids



if __name__ == "__main__":
    parsed_ids = parse_ids()
    ranges = get_ranges(parsed_ids)
    sum_of_invalids = find_invalid_ids(ranges)
    print(sum_of_invalids)

