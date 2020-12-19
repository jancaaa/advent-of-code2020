import collections
import re


def read_file(file: str) -> (dict, list):
    with open(file) as fp:
        rules = collections.defaultdict(list)
        line = fp.readline().strip()
        while line:
            i, rule = line.split(":")
            rules[int(i)] = rule.strip().replace("\"", "")
            line = fp.readline().strip()

        messages = []
        line = fp.readline().strip()
        while line:
            messages.append(line)
            line = fp.readline().strip()
    return rules, messages


def tests():
    rules, messages = read_file("test_input_part1.txt")
    assert part1(rules, messages) == 2

    rules, messages = read_file("test_input_part2.txt")
    assert part2(rules, messages) == 12


def create_regex(string: str, rules: dict) -> str:
    if string == "a" or string == "b":
        return string
    else:
        parts = string.split(" | ")
        res = []
        for part in parts:
            literals = part.split(" ")
            s = ""
            for l in literals:
                s += create_regex(rules[int(l)], rules)
            res.append(s)
        return "(?:" + "|".join(res) + ")"


def process_cycling(string: str, cycling_literals: list, rules: dict) -> str:
    if string == "8":
        return create_regex_with_loops("42", cycling_literals, rules) + "+"
    elif string == "11":
        r42 = create_regex_with_loops("42", cycling_literals, rules)
        r31 = create_regex_with_loops("31", cycling_literals, rules)
        return "(?:" + "|".join(f"{r42}{{{n}}}{r31}{{{n}}}" for n in range(1, 100)) + ")"


def create_regex_with_loops(string: str, cycling_literals: list, rules: dict) -> str:
    if string == "a" or string == "b":
        return string
    else:
        parts = string.split(" | ")
        res = []
        for part in parts:
            literals = part.split(" ")
            s = ""
            for l in literals:
                if l in cycling_literals:
                    s += process_cycling(l, cycling_literals, rules)
                else:
                    s += create_regex_with_loops(rules[int(l)], cycling_literals, rules)
            res.append(s)
        return "(?:" + "|".join(res) + ")"


def part1(rules: dict, messages: list) -> int:
    regex = create_regex(rules[0], rules)

    count = 0
    for m in messages:
        if re.fullmatch(regex, m):
            count += 1
    return count


def part2(rules: dict, messages: list) -> int:
    cycling_literals = ["8", "11"]
    regex = create_regex_with_loops(rules[0], cycling_literals, rules)

    count = 0
    for m in messages:
        if re.fullmatch(regex, m):
            count += 1
    return count


if __name__ == "__main__":
    tests()
    rules, messages = read_file("input.txt")
    print(f"Part 1: {part1(rules, messages)}")
    print(f"Part 2: {part2(rules, messages)}")
