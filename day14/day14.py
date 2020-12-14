import collections


def read_file(file: str) -> list:
    with open(file) as fp:
        line = fp.readline().rstrip()
        input = []
        record = {}
        while line:
            line = line.split(" = ")
            if line[0] == "mask":
                if record != {}:
                    input.append(record)
                    record = {}

                record["mask"] = line[1]
                record["instructions"] = []
            else:
                pos = ''.join(x for x in line[0] if x.isdigit())
                value = line[1]
                record["instructions"].append((int(pos), int(value)))
            line = fp.readline().rstrip()
        input.append(record)
    return input


def apply_mask_part1(value: int, mask: str) -> int:
    value = bin(value)[2:].zfill(36)

    result = list(value)
    for i in range(36):
        if mask[i] != 'X':
            result[i] = mask[i]
    result = "".join(result)
    return int(result, 2)


def apply_mask_part2(value: int, mask: str) -> str:
    value = bin(value)[2:].zfill(36)

    result = list(mask)
    for i in range(36):
        if mask[i] == '0':
            result[i] = value[i]
    return "".join(result)


def generate_possible_combinations(value: str) -> list:
    value = value.lstrip("0")
    result = []

    if value.find("X") == -1:
        result.append(value)
    else:
        index = value.index("X")
        replaced = replaceX(value, index)

        for i in replaced:
            result.extend(generate_possible_combinations(i))
    return result


def replaceX(value: str, index: int) -> list:
    result = []
    v = list(value)
    for i in [0, 1]:
        v[index] = str(i)
        result.append("".join(v))
    return result


def tests():
    assert part1(read_file("test_input_part1.txt")) == 165
    assert part2(read_file("test_input_part2.txt")) == 208


def part1(input: list) -> int:
    mem = collections.defaultdict(int)
    for i in input:
        mask = i["mask"]
        for pos, value in i["instructions"]:
            mem[pos] = apply_mask_part1(value, mask)
    return sum(mem.values())


def part2(input: list) -> int:
    mem = collections.defaultdict(int)
    for i in input:
        mask = i["mask"]
        for pos, value in i["instructions"]:
            v = apply_mask_part2(pos, mask)
            combinations = generate_possible_combinations(v)
            for j in combinations:
                mem[j] = value
    return sum(mem.values())


if __name__ == "__main__":
    tests()
    input = read_file("input.txt")
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
