def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline().rstrip()
        entries = []
        while line:
            entries.append(split_line(line))
            line = fp.readline().rstrip()
    return entries


def split_line(line: str) -> dict:
    """
    :param line: format: 1-3 a: abcde
    """
    record = {}
    parts = line.split(':')
    record["password"] = parts[1].strip()
    parts = parts[0].split(' ')
    record["letter"] = parts[1]
    parts = parts[0].split('-')
    record["low"] = int(parts[0])
    record["high"] = int(parts[1])
    return record


def get_count(string: str, letter: str):
    """
    Get count of :param letter in :param string
    """
    count = 0
    for x in string:
        if x == letter:
            count += 1
    return count


def has_valid_letter_count(record: dict) -> bool:
    count = get_count(record["password"], record["letter"])
    return record["low"] <= count <= record["high"]


def has_valid_letter_positions(record: dict) -> bool:
    password = record["password"]
    letter = record["letter"]
    return (password[record["low"] - 1] == letter) ^ (password[record["high"] - 1] == letter)


def part1(entries: list) -> int:
    valid_count = 0
    for x in entries:
        if has_valid_letter_count(x):
            valid_count += 1
    return valid_count


def part2(entries: list) -> int:
    valid_count = 0
    for x in entries:
        if has_valid_letter_positions(x):
            valid_count += 1
    return valid_count


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
