def read_file(file: str) -> list:
    with open(file) as fp:
        line = fp.readline().rstrip()
        lines = []
        while line:
            lines.append(int(line))
            line = fp.readline().rstrip()
    return lines


def tests():
    lines = read_file("test_input.txt")
    assert part1(lines, 5) == 127
    assert part2(127, lines) == 62


def is_sum_of_two_in_range(lines: list, from_line: int, to_line: int, sum: int):
    for i in range(from_line, to_line - 1):
        for j in range(from_line + 1, to_line):
            if lines[i] + lines[j] == sum:
                return True
    return False


def part1(lines: list, preambule_len=25) -> int:
    for i in range(preambule_len, len(lines)):
        if not is_sum_of_two_in_range(lines, i - preambule_len, i, lines[i]):
            return lines[i]


def part2(expected_sublist_sum: int, lines: list) -> int:
    for i in range(len(lines)):
        sub_list = []
        j = i
        while sum(sub_list) < expected_sublist_sum:
            sub_list.append(lines[j])
            j += 1
        if sum(sub_list) == expected_sublist_sum:
            return min(sub_list) + max(sub_list)


if __name__ == "__main__":
    tests()
    lines = read_file("input.txt")
    p1 = part1(lines)
    print(f"Part 1: {p1}")
    print(f"Part 2: {part2(p1, lines)}")
