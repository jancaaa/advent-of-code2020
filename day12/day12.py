def read_file(file: str) -> list:
    with open(file) as fp:
        line = fp.readline().rstrip()
        instructions = []
        while line:
            instructions.append(line)
            line = fp.readline().rstrip()
    return instructions


def tests():
    instructions = read_file("test_input.txt")
    assert part1(instructions) == 25
    assert part2(instructions) == 286


def process_instruction_part1(ship_pos: list, instruction: str) -> list:
    d = instruction[0]
    n = int(instruction[1:])
    if d == "N":
        ship_pos["NS"] += n
    elif d == "S":
        ship_pos["NS"] -= n
    elif d == "E":
        ship_pos["WE"] += n
    elif d == "W":
        ship_pos["WE"] -= n

    elif d == "F":
        process_instruction_part1(ship_pos, ship_pos["direction"] + str(n))

    elif d == "L" or d == "R":
        ship_pos = rotate_ship(ship_pos, instruction)

    return ship_pos


def rotate_ship(ship: list, instruction: str) -> list:
    d = instruction[0]
    n = int(instruction[1:])
    if d == "L":
        n = 360 - n
    for i in range(n // 90):
        ship["direction"] = rotate_90deg_right(ship["direction"])
    return ship


def rotate_90deg_right(d: chr) -> chr:  # +90
    if d == "N":
        return "E"
    elif d == "E":
        return "S"
    elif d == "S":
        return "W"
    elif d == "W":
        return "N"


def process_instruction_part2(ship_pos, waypoint, instruction) -> list:
    d = instruction[0]
    n = int(instruction[1:])

    if d == "N":
        waypoint["NS"] += n
    elif d == "S":
        waypoint["NS"] -= n
    elif d == "E":
        waypoint["WE"] += n
    elif d == "W":
        waypoint["WE"] -= n

    elif d == "F":
        ship_pos["WE"] += n * waypoint["WE"]
        ship_pos["NS"] += n * waypoint["NS"]

    elif d == "L" or d == "R":
        waypoint = rotate_waypoint_around_ship(waypoint, instruction)

    return ship_pos, waypoint


def rotate_waypoint_around_ship(waypoint: list, instruction: str) -> list:
    d = instruction[0]
    n = int(instruction[1:])
    if d == "L":
        n = 360 - n
    for i in range(n // 90):
        waypoint = {"WE": waypoint["NS"], "NS": -1 * waypoint["WE"]}
    return waypoint


def part1(instructions: list) -> int:
    ship_pos = {"direction": "E", "WE": 0, "NS": 0}

    for i in instructions:
        ship_pos = process_instruction_part1(ship_pos, i)

    return abs(ship_pos["WE"]) + abs(ship_pos["NS"])


def part2(instructions: list) -> int:
    ship_pos = {"WE": 0, "NS": 0}
    waypoint = {"WE": 10, "NS": 1}

    for i in instructions:
        ship_pos, waypoint = process_instruction_part2(ship_pos, waypoint, i)

    return abs(ship_pos["WE"]) + abs(ship_pos["NS"])


if __name__ == "__main__":
    tests()
    instructions = read_file("input.txt")
    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")
