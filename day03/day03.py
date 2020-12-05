def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        map = []
        while line:
            map.append(line.rstrip())
            line = fp.readline()
    return map


def get_x_position(i: int, offset: int) -> int:
    return (i * offset) % 31


def is_tree(map: list, x: int, y: int) -> bool:
    return map[y][x] == "#"


def part1(map: list):
    tree_count = 0
    for i in range(len(map)):
        x = get_x_position(i, 3)
        if is_tree(map, x, i):
            tree_count += 1
    return tree_count


def part2(map: list):
    product = 1
    offsets = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for o in offsets:
        i = 0
        y = 0
        tree_count = 0
        while y < len(map):
            x = get_x_position(i, o[0])
            if is_tree(map, x, y):
                tree_count += 1
            y += o[1]
            i += 1
        product *= tree_count
    return product


if __name__ == "__main__":
    map = read_file()
    print(f"Part 1: {part1(map)}")
    print(f"Part 2: {part2(map)}")
