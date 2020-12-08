from copy import deepcopy


def read_file(file: str) -> list:
    with open(file) as fp:
        line = fp.readline().rstrip()
        lines = []
        while line:
            instruction, arg = line.split(" ")
            record = {"instruction": instruction, "arg": int(arg)}
            lines.append(record)
            line = fp.readline().rstrip()
    return lines


def prepare_program(lines: list, line: int, instruction: str) -> list:
    program = deepcopy(lines)
    arg = lines[line]["arg"]
    program[line] = {"instruction": instruction, "arg": arg}
    return program


def play(lines: list) -> int:
    acc = 0
    i = 0
    x = lines[i]
    while not x.get("seen"):
        x["seen"] = True
        if x["instruction"] == 'acc':
            acc += x["arg"]
            i += 1
        elif x["instruction"] == 'jmp':
            i += x["arg"]
        else:
            i += 1

        if i == len(lines):
            return acc
        else:
            x = lines[i]
    return None


def tests():
    lines = read_file("test_input.txt")
    assert part1(deepcopy(lines)) == 5
    assert part2(lines) == 8


def part1(lines: list) -> int:
    acc = 0
    i = 0
    x = lines[i]
    while not x.get("seen"):
        x["seen"] = True

        if x["instruction"] == 'acc':
            acc += x["arg"]
            i += 1
        elif x["instruction"] == 'jmp':
            i += x["arg"]
        else:
            i += 1
        x = lines[i]
    return acc


def part2(lines: list) -> int:
    for i in range(len(lines)):
        instruction = lines[i]["instruction"]
        if instruction == "nop":
            program = prepare_program(lines, i, "jmp")
            acc = play(program)
        elif instruction == "jmp":
            program = prepare_program(lines, i, "nop")
            acc = play(program)
        else:
            acc = None

        if acc:
            return acc


if __name__ == "__main__":
    tests()
    lines = read_file("input.txt")
    print(f"Part 1: {part1(deepcopy(lines))}")
    print(f"Part 2: {part2(lines)}")
