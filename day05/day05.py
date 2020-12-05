def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        items = []
        while line:
            items.append(line.rstrip())
            line = fp.readline()
    return items


def tests():
    assert get_seat_id('FBFBBFFRLR') == 357
    assert get_seat_id('BFFFBBFRRR') == 567
    assert get_seat_id('FFFBBBFRRR') == 119
    assert get_seat_id('BBFFBBFRLL') == 820


def get_seat_id(code: str) -> int:
    low = 0
    high = 127
    for x in code[:7]:
        midpoint = get_midpoint(low, high)
        if x == "F":
            high = high - midpoint
        elif x == "B":
            low = low + midpoint
    row_id = low

    low = 0
    high = 7
    for x in code[-3:]:
        midpoint = get_midpoint(low, high)
        if x == "L":
            high = high - midpoint
        elif x == "R":
            low = low + midpoint
    column_id = low
    return row_id * 8 + column_id


def get_midpoint(low: int, high: int) -> int:
    r = high - low + 1
    return r // 2


def part1(items: list):
    highest_id = 0
    for i in items:
        seat_id = get_seat_id(i)
        if seat_id > highest_id:
            highest_id = seat_id
    return highest_id


def part2(items: list):
    seats = []
    for i in items:
        seat_id = get_seat_id(i)
        seats.append(seat_id)
    for i in range(min(seats) + 1, max(seats) - 1):
        if i not in seats and i - 1 in seats and i + 1 in seats:
            return i


if __name__ == "__main__":
    items = read_file()
    tests()
    print(f"Part 1: {part1(items)}")
    print(f"Part 2: {part2(items)}")
