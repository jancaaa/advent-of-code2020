from copy import deepcopy


def tests():
    input = '389125467'
    input = [int(i) for i in input]

    assert part1(input) == '67384529'


def get_destination_index(input: list, current: int) -> int:
    destination = current - 1
    while destination >= min(input):
        if destination in input:
            return input.index(destination)
        else:
            destination = destination - 1

    # there is no cup with lower value
    destination = max(input)
    return input.index(destination)


def get_index_of_current(input: list, current: int) -> int:
    current_index = input.index(current)
    current_index = current_index + 1
    if current_index == len(input):
        # current was the last one -> move to the beginning
        current_index = 0
    return current_index


def remove_cups(input: list, current_index: int) -> (list, list):
    removed_cups = []
    to_be_removed = current_index + 1
    for i in range(3):  # remove next 3 caps
        if to_be_removed < len(input):
            removed = input.pop(to_be_removed)
        else:
            removed = input.pop(0)
        removed_cups.append(removed)
    return input, removed_cups


def insert_cups(input: list, destination: int, cups: list) -> list:
    for i in reversed(cups):
        input.insert(destination + 1, i)
    return input


def shift(input: list) -> list:
    one = input.index(1)
    return input[one + 1:] + input[:one]


def part1(input: list) -> str:
    current_index = 0
    current = input[current_index]
    for _ in range(100):
        input, removed_cups = remove_cups(input, current_index)
        destination_index = get_destination_index(input, current)
        input = insert_cups(input, destination_index, removed_cups)
        current_index = get_index_of_current(input, current)
        current = input[current_index]

    shifted = shift(input)
    for i in range(len(shifted)):
        shifted[i] = str(shifted[i])
    return "".join(shifted)


def part2(input: list) -> int:
    return


if __name__ == "__main__":
    tests()
    input = '469217538'
    input = [int(i) for i in input]

    print(f"Part 1: {part1(deepcopy(input))}")
    # print(f"Part 2: {part2(input)}")
