from copy import deepcopy


def read_file(file: str) -> list:
    with open(file) as fp:
        line = fp.readline().rstrip()
        seats = []
        while line:
            line = list(line)
            seats.append(line)
            line = fp.readline().rstrip()
    return seats


def tests():
    seats = read_file("test_input.txt")
    assert part1(seats) == 37
    assert part2(seats) == 26


def get_adjacent_seats(seats: list, i: int, j: int) -> list:
    adjacent_seats = []

    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            xi = i + x
            yj = j + y
            if xi == i and yj == j:
                continue  # actual seat
            elif 0 <= xi < len(seats) and 0 <= yj < len(seats[i]):
                adjacent_seats.append(seats[xi][yj])
    return adjacent_seats


def apply_part1_rules(seats: list) -> list:
    updated = deepcopy(seats)
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j] != '.':
                adjacent_occupied_seats_count = get_adjacent_seats(seats, i, j).count("#")
                if seats[i][j] == "L" and adjacent_occupied_seats_count == 0:
                    updated[i][j] = "#"
                elif seats[i][j] == "#" and adjacent_occupied_seats_count >= 4:
                    updated[i][j] = "L"
    return updated


def get_first_seen_seats(seats: list, i: int, j: int) -> list:
    first_seen_seats = []

    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            xi = i + x
            yj = j + y
            if xi == i and yj == j:
                continue  # actual seat
            else:
                while 0 <= xi < len(seats) and 0 <= yj < len(seats[i]):
                    if seats[xi][yj] != ".":
                        first_seen_seats.append(seats[xi][yj])
                        break
                    else:
                        # move in given direction
                        xi += x
                        yj += y
    return first_seen_seats


def apply_part2_rules(seats: list) -> list:
    updated = deepcopy(seats)
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j] != '.':
                first_seen_occupied_seats_count = get_first_seen_seats(seats, i, j).count("#")
                if seats[i][j] == "L" and first_seen_occupied_seats_count == 0:
                    updated[i][j] = "#"
                elif seats[i][j] == "#" and first_seen_occupied_seats_count >= 5:
                    updated[i][j] = "L"
    return updated


def count_occupied(seats: list) -> int:
    occupied_count = 0
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j] == "#":
                occupied_count += 1
    return occupied_count


def part1(seats: list) -> int:
    previous = seats
    current = apply_part1_rules(seats)
    while current != previous:
        previous = current
        current = apply_part1_rules(previous)
    return count_occupied(current)


def part2(seats: list) -> int:
    previous = seats
    current = apply_part2_rules(seats)
    while current != previous:
        previous = current
        current = apply_part2_rules(previous)
    return count_occupied(current)


if __name__ == "__main__":
    tests()
    seats = read_file("input.txt")
    print(f"Part 1: {part1(seats)}")
    print(f"Part 2: {part2(seats)}")
