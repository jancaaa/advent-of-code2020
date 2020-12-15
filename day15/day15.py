import collections


def read_file(file: str) -> list:
    with open(file) as fp:
        line = fp.readline().rstrip()
        input = []
        line = line.split(",")
        for i in line:
            input.append(int(i))
    return input


def tests():
    input = read_file("test_input.txt")
    assert part1(input) == 436
    assert part2(input) == 175594


def next_number(positions: dict, last: int) -> int:
    if len(positions[last]) == 1:
        x = 0
    else:
        x = positions[last][-1] - positions[last][-2]
    return x


def play(input: list, round_count: int) -> int:
    positions = collections.defaultdict(list)

    for i, n in enumerate(input):
        positions[n] = [i]

    last = input[-1]
    for i in range(len(input), round_count):
        last = next_number(positions, last)
        positions[last].append(i)
    return last


def part1(input: list) -> int:
    return play(input, 2020)


def part2(input: list) -> int:
    return play(input, 30000000)


if __name__ == "__main__":
    tests()
    input = read_file("input.txt")
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
