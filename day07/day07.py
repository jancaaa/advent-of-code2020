def read_file(file) -> dict:
    with open(file) as fp:
        line = fp.readline().rstrip()
        rules = {}
        while line:
            bag, content = process_line(line)
            rules[bag] = content
            line = fp.readline().rstrip()
    return rules


def process_line(line: str) -> dict:
    line = line[:-1]  # remove dot
    line = line.replace("bags", "")
    line = line.replace("bag", "")
    bag, bag_content = line.split("contain")
    bag_content = bag_content.split(",")
    processed_content = []
    for c in bag_content:
        c = c.strip()
        if c != 'no other':
            c = c.split(None, 1)
            record = {"count": int(c[0]), "color": c[1]}
            processed_content.append(record)
    return bag.strip(), processed_content


def contains_shiny_gold(bag: str, rules: dict) -> bool:
    if bag == 'shiny gold':
        return True
    elif not bag:  # []
        return False
    else:
        for b in rules[bag]:
            x = contains_shiny_gold(b["color"], rules)
            if x:
                return True
        return False


def content_count(color: str, rules: dict) -> int:
    count = 0
    content = rules[color]
    for c in content:
        count += c["count"] + c["count"] * content_count(c["color"], rules)
    return count


def tests():
    rules = read_file("test_input.txt")
    assert content_count("faded blue", rules) == 0
    assert content_count("dotted black", rules) == 0
    assert content_count("vibrant plum", rules) == 11
    assert content_count("dark olive", rules) == 7
    assert content_count("shiny gold", rules) == 32


def part1(rules: dict) -> int:
    count = 0
    for color in rules.keys():
        if color != 'shiny gold' and contains_shiny_gold(color, rules):
            count += 1
    return count


def part2(rules: dict) -> int:
    return content_count('shiny gold', rules)


if __name__ == "__main__":
    tests()
    rules = read_file("input.txt")
    print(f"Part 1: {part1(rules)}")
    print(f"Part 2: {part2(rules)}")
