def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            entries.append(int(line.rstrip()))
            line = fp.readline()
        return entries


def part1(entries: list) -> int:
    for x in entries:
        for y in entries:
            if x + y == 2020:
                return x * y


def part2(entries: list) -> int:
    for x in entries:
        for y in entries:
            for z in entries:
                if x + y + z == 2020:
                    return x * y * z


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
