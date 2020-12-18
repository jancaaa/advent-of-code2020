def read_file(file: str):
    with open(file) as fp:
        line = fp.readline().rstrip()
        input = []
        while line:
            input.append(line)
            line = fp.readline().rstrip()
    return input


def tests():
    assert calculate_part1("1 + 2 * 3 + 4 * 5 + 6") == 71
    assert calculate_part1("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert calculate_part1("2 * 3 + (4 * 5)") == 26
    assert calculate_part1("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
    assert calculate_part1("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
    assert calculate_part1("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632

    assert calculate_part2("1 + 2 * 3 + 4 * 5 + 6") == 231
    assert calculate_part2("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert calculate_part2("2 * 3 + (4 * 5)") == 46
    assert calculate_part2("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
    assert calculate_part2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
    assert calculate_part2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340


def get_bracket(string: str) -> str:
    end = string.find(")") + 1
    begin = string[:end].rfind("(")
    substring = string[begin:end]
    return substring  # including brackets


def calculate_part1(string: str) -> int:
    substring = get_bracket(string)
    if substring:
        bracket_result = calculate_part1(substring[1:-1])
        return calculate_part1(string.replace(substring, str(bracket_result)))
    else:
        return _calculate_part1(string)


def _calculate_part1(string: str) -> int:
    parts = string.split(" ")
    while 1 < len(parts):
        if parts[1] == '+':
            parts[0] = str(int(parts[0]) + int(parts[2]))
        elif parts[1] == '*':
            parts[0] = str(int(parts[0]) * int(parts[2]))

        del parts[2]
        del parts[1]

    return int(parts[0])


def calculate_part2(string: str) -> int:
    substring = get_bracket(string)
    if substring:
        bracket_result = calculate_part2(substring[1:-1])
        return calculate_part2(string.replace(substring, str(bracket_result)))
    else:
        return _calculate_part2(string)


def _calculate_part2(string: str) -> int:
    parts = string.split(" ")

    i = _addition_index(parts)
    while i != -1:
        result = str(int(parts[i - 1]) + int(parts[i + 1]))
        parts[i - 1] = result
        del parts[i + 1]
        del parts[i]
        i = _addition_index(parts)

    while 1 < len(parts):
        parts[0] = str(int(parts[0]) * int(parts[2]))
        del parts[2]
        del parts[1]

    return int(parts[0])


def _addition_index(parts: list) -> int:
    try:
        return parts.index("+")
    except ValueError:
        return -1


def part1(input: list) -> int:
    sum = 0
    for i in input:
        sum += calculate_part1(i)
    return sum


def part2(input: list) -> int:
    sum = 0
    for i in input:
        sum += calculate_part2(i)
    return sum


if __name__ == "__main__":
    tests()
    input = read_file("input.txt")
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
