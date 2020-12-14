def read_file(file: str) -> list:
    with open(file) as fp:
        timestamp = int(fp.readline().rstrip())
        departures = fp.readline().rstrip().split(",")
        processed_departures = []
        for d in departures:
            if d == "x":
                processed_departures.append("x")
            else:
                processed_departures.append(int(d))
    return timestamp, processed_departures


def tests():
    timestamp, departures = read_file("test_input.txt")
    assert part1(timestamp, departures) == 295


def part1(timestamp: int, departures: list) -> int:
    next_departures = []
    for d in departures:
        if (d != "x"):
            previous_departure = timestamp // d * d
            next_departure = previous_departure + d
            next_departures.append({"line": d, "next_departure": next_departure})

    first_departure = min([i["next_departure"] for i in next_departures])
    bus = next(i["line"] for i in next_departures if i["next_departure"] == first_departure)
    return (first_departure - timestamp) * bus


def part2_generate_formula(departures: list) -> str:
    formula = ""
    for i, d in enumerate(departures):
        if d != "x":
            if i != 0:
                formula += " and "
            formula += f"(x+{i})%{d}"
    return formula


def inv(a, m):
    m0 = m
    x0 = 0
    x1 = 1

    if (m == 1):
        return 0

    # Apply extended Euclid Algorithm
    while (a > 1):
        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as euclid's algo
        m = a % m
        a = t

        t = x0

        x0 = x1 - q * x0

        x1 = t

        # Make x1 positive
    if (x1 < 0):
        x1 = x1 + m0

    return x1


def part2(departures: list) -> int:
    """
    Solution using Chinese remainder theorem (https://en.wikipedia.org/wiki/Chinese_remainder_theorem)
    """
    prod = 1
    for i, d in enumerate(departures):
        if d != "x":
            prod *= d

    total = 0

    for i, d in enumerate(departures):
        if d != "x":
            pp = prod // d
            total += (d - i) * pp * pow(pp, d - 2, d)
            total %= prod
    return total


if __name__ == "__main__":
    tests()

    timestamp, departures = read_file("input.txt")
    print(f"Part 1: {part1(timestamp, departures)}")
    print(f"Part 2 - WolframAlpha formula: {part2_generate_formula(departures)}")
    print(f"Part 2: {part2(departures)}")
