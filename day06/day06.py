def read_file() -> list:
    with open("input.txt") as fp:
        items = []
        for record in fp.read().split("\n\n"):
            record = record.replace("\n", " ")
            items.append(record)
    return items


def tests():
    assert unique_letters_count("abc") == 3
    assert unique_letters_count("abac") == 3
    assert unique_letters_count("aaaa") == 1
    assert unique_letters_count("b") == 1

    assert letters_in_all_substrings_count("abc") == 3
    assert letters_in_all_substrings_count("a b c") == 0
    assert letters_in_all_substrings_count("ab ac") == 1
    assert letters_in_all_substrings_count("a a a a") == 1
    assert letters_in_all_substrings_count("b") == 1


def unique_letters_count(string: str) -> int:
    letters = set()
    for letter in string:
        if letter not in letters:
            letters.add(letter)
    return len(letters)


def letters_in_all_substrings_count(string: str) -> int:
    count = 0
    substrings = string.split(" ")
    for letter in substrings[0]:
        in_all = True
        for s in substrings[1:]:
            if letter not in s:
                in_all = False
                break
        if in_all:
            count += 1
    return count


def part1(items: list) -> int:
    sum = 0
    for i in items:
        count = unique_letters_count(i.replace(" ", ""))
        sum += count
    return sum


def part2(items: list) -> int:
    sum = 0
    for i in items:
        count = letters_in_all_substrings_count(i)
        sum += count
    return sum


if __name__ == "__main__":
    items = read_file()
    tests()
    print(f"Part 1: {part1(items)}")
    print(f"Part 2: {part2(items)}")
