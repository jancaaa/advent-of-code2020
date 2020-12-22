from copy import deepcopy


def read_file(file: str) -> list:
    with open(file) as fp:
        input = []
        line = fp.readline().rstrip()
        while line:
            input.append(list(line))
            line = fp.readline().rstrip()
    return [input]


def tests():
    input = read_file("test_input.txt")
    assert part1(input) == 112


def add_inactive_around(input: list) -> list:
    for z in range(len(input)):
        for y in input[z]:
            y.insert(0, '.')  # add y -1
            y.append('.')  # add y+1

        input[z].insert(0, ['.' for _ in range(len(input[z][0]))])  # add x -1
        input[z].insert(len(input[z]), ['.' for _ in range(len(input[z][0]))])  # add x +1

    new_z = []
    for _ in range(len(input[0])):
        new_z.append(['.' for _ in range(len(input[0][0]))])

    input.insert(0, deepcopy(new_z))  # add z-1
    input.insert(len(input), deepcopy(new_z))  # add z+1

    return input


def simulate_cycle(input: list) -> list:
    output = deepcopy(input)
    for z in range(len(input)):
        for y in range(len(input[z])):
            for x in range(len(input[z][y])):
                current = input[z][y][x]
                neighbours = get_neighbors(x, y, z, input)
                active_neighbours_count = neighbours.count("#")

                if current == "#" and not (active_neighbours_count == 2 or active_neighbours_count == 3):
                    output[z][y][x] = '.'
                elif current == '.' and active_neighbours_count == 3:
                    output[z][y][x] = '#'
    return output


def get_neighbors(x: int, y: int, z: int, input: list) -> list:
    neighbors = []
    for oz in (-1, 0, 1):
        for oy in (-1, 0, 1):
            for ox in (-1, 0, 1):
                xi = x + ox
                yi = y + oy
                zi = z + oz
                if xi == x and yi == y and zi == z:
                    continue  # actual cube
                elif 0 <= zi < len(input) and 0 <= yi < len(input[0]) and 0 <= xi < len(input[0][0]):
                    neighbors.append(input[zi][yi][xi])
    return neighbors


def part1(input: list) -> int:
    for i in range(6):
        input = add_inactive_around(input)
        input = simulate_cycle(input)

    count = 0
    for z in range(len(input)):
        for y in range(len(input[z])):
            for x in range(len(input[z][y])):
                current = input[z][y][x]
                if current == "#":
                    count += 1
    return count


def part2(input: list) -> int:
    return


if __name__ == "__main__":
    tests()
    input = read_file("input.txt")
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
