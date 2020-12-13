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


def part2(departures: list) -> int:
    return


if __name__ == "__main__":
    tests()

    timestamp, departures = read_file("input.txt")
    print(f"Part 1: {part1(timestamp, departures)}")
    print(f"Part 2: {part2(departures)}")
