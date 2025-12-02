
DAY_ONE_INPUT = "Day One/Puzzle Inputs/day1.txt"
LEFT, RIGHT = "L", "R"


def read_safe_instructions():
    passcode, dial = 0, 50
    
    with open(DAY_ONE_INPUT) as file:
        for line in file:
            line = line.strip()
            direction = line[0]
            number = int(line[1:])
            
            if direction == "L":
                dial = move_dial(dial, -number)
            if direction == "R":
                dial = move_dial(dial, number)
            if dial == 0:
                passcode += 1
    return passcode


def move_dial(dial, number):
    return (dial + number) % 100

if __name__ == "__main__":
    print(read_safe_instructions())