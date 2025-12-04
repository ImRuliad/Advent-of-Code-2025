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
            ranges.append(number)
    return ranges

def is_invalid(number):
    len_num = len(number)
    mid = len_num // 2
      
    for curr_len in range(1, mid + 1):
        prefix = number[:curr_len]
        if prefix * (len_num // curr_len) == number:
            return True
    return False
        
def find_invalid_ids(ranges):
    sum_of_invalids = 0
    for number in ranges:
        if is_invalid(str(number)):
            sum_of_invalids += number
    return sum_of_invalids

if __name__ == "__main__":
    parsed_ids = parse_ids()
    ranges = get_ranges(parsed_ids)
    sum_of_invalids = find_invalid_ids(ranges)
    print(sum_of_invalids)

