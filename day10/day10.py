def read_file(file: str) -> list:
    with open(file) as fp:
        line = fp.readline().rstrip()
        lines = []
        while line:
            lines.append(int(line))
            line = fp.readline().rstrip()
    return lines


def tests():
    short_input = read_file("test_input_short.txt")
    long_input = read_file("test_input_long.txt")

    assert part1(sorted(short_input)) == 35
    assert part1(sorted(long_input)) == 220

    assert part2(sorted(short_input)) == 8
    assert part2(sorted(long_input)) == 19208


def part1(lines: list) -> int:
    j1 = 0
    j3 = 1
    current = 0
    for i in lines:
        if current + 1 == i:
            j1 += 1
        elif current + 3 == i:
            j3 += 1
        current = i
    return j1 * j3


counts_cache = {}
def count(lines: list, i: int) -> int:
    if i == len(lines) - 1:
        return 1
    c = 0
    j = i + 1
    while j < len(lines) and 1 <= lines[j] - lines[i] <= 3:
        if j not in counts_cache.keys():
            counts_cache[j] = count(lines, j)

        c += counts_cache[j]
        j += 1
    return c


def part2(lines: list) -> int:
    counts_cache.clear()
    return count([0] + lines, 0)


if __name__ == "__main__":
    tests()
    lines = read_file("input.txt")
    lines.sort()
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
