import collections


def read_file(file: str) -> (dict, list, list):
    with open(file) as fp:
        line = fp.readline()
        rules = {}
        while line:
            name, range_string = line.split(":")
            ranges = []
            for r in range_string.split("or"):
                range_from, range_to = r.split("-")
                ranges.append((int(range_from), int(range_to)))
            rules[name] = ranges
            line = fp.readline()[:-1]

        fp.readline()  # your ticket

        line = fp.readline().split(",")
        my_ticket = [int(i) for i in line]

        fp.readline()  # empty line
        fp.readline()  # nearby tickets

        line = fp.readline()
        nearby_tickets = []
        while line:
            line = line.split(",")
            nearby_tickets.append([int(i) for i in line])
            line = fp.readline()
    return rules, my_ticket, nearby_tickets


def tests():
    rules, my_ticket, nearby_tickets = read_file("test_input_part1.txt")
    assert part1(rules, nearby_tickets) == 71

    rules, my_ticket, nearby_tickets = read_file("test_input_part2.txt")
    positions = get_positions(rules, get_possible_positions(rules, nearby_tickets))
    assert my_ticket[positions['class']] == 12
    assert my_ticket[positions['row']] == 11
    assert my_ticket[positions['seat']] == 13


def is_in_range(value: int, ranges: dict) -> bool:
    for r1, r2 in ranges:
        if value in range(r1, r2 + 1):
            return True
    return False


def matches_rule(value: int, rules: dict) -> bool:
    for p in rules:
        if is_in_range(value, rules[p]):
            return True
    return False


valid_tickets = []


def part1(rules: dict, nearby_tickets: list) -> int:
    valid_tickets.clear()
    invalid_sum = 0

    for ticket in nearby_tickets:
        valid = True
        for i in ticket:
            if not matches_rule(i, rules):
                valid = False
                invalid_sum += i

        if valid:
            valid_tickets.append(ticket)

    return invalid_sum


def get_possible_positions(rules: dict, tickets: list) -> dict:
    possible_positions = collections.defaultdict(list)

    for rule in rules:
        for i in range(len(rules)):
            can_be = True
            for t in tickets:
                if not is_in_range(t[i], rules[rule]):
                    can_be = False
                    break
            if can_be:
                possible_positions[i].append(rule)
    return possible_positions


def get_positions(rules: dict, possible_positions: dict) -> dict:
    positions = {}
    while len(positions) < len(rules):
        for i in possible_positions:
            if len(possible_positions[i]) == 1:
                placed = possible_positions[i][0]
                positions[placed] = i
                for j in possible_positions:  # remove from other positions
                    try:
                        possible_positions[j].remove(placed)
                    except ValueError:
                        pass
    return positions


def part2(rules: dict, my_ticket: list, nearby_tickets: list) -> int:
    possible_positions = get_possible_positions(rules, nearby_tickets)
    positions = get_positions(rules, possible_positions)

    product = 1
    for p in positions:
        if p.startswith("departure"):
            product *= int(my_ticket[positions[p]])
    return product


if __name__ == "__main__":
    tests()
    rules, my_ticket, nearby_tickets = read_file("input.txt")
    print(f"Part 1: {part1(rules, nearby_tickets)}")
    print(f"Part 2: {part2(rules, my_ticket, valid_tickets)}")
