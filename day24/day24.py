import collections


def read_file(file: str) -> (list, list):
    with open(file) as fp:
        line = fp.readline().rstrip()
        input = []

        while line:
            line = line.replace("e", "e ").replace("w", "w ").strip()
            line = line.split(" ")
            input.append(line)
            line = fp.readline().rstrip()
    return input


def tests():
    input = read_file("test_input.txt")
    assert part1(input) == 10


def move(x: int, y: int, direction: str) -> (int, int):  # get coordinates (x, y) of tile in given direction
    if direction == "e":
        return x + 1, y
    elif direction == "w":
        return x - 1, y

    if direction.endswith("w"):
        if y % 2 == 0:
            x = x - 1
        else:
            x = x
    elif direction.endswith("e"):
        if y % 2 == 0:
            x = x
        else:
            x = x + 1

    if direction.startswith("n"):
        y = y + 1
    elif direction.startswith("s"):
        y = y - 1

    return x, y


def build_floor(input: list) -> dict:
    floor = collections.defaultdict(dict)

    for line in input:
        x, y = 0, 0  # starting point
        for i in line:
            x, y = move(x, y, i)

        if x in floor[y].keys():
            if floor[y][x] == "W":
                floor[y][x] = "B"
            else:
                floor[y][x] = "W"

        else:
            # is white by default
            floor[y][x] = "B"
    return floor


def count_black_tiles(floor: dict) -> int:
    count = 0
    for y in floor:
        for x in floor[y]:
            if floor[y][x] == "B":
                count += 1
    return count


def part1(input: list) -> int:
    floor = build_floor(input)
    return count_black_tiles(floor)


def part2(input: list) -> int:
    return


if __name__ == "__main__":
    tests()
    input = read_file("input.txt")
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
