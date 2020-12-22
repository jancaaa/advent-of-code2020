import re


def read_file(file: str) -> dict:
    with open(file) as fp:
        tiles = {}
        file_content = fp.read().split('\n\n')
        for tile in file_content:
            tile = tile.split('\n')
            id = re.search(r'\d+', tile[0]).group(0)
            tiles[int(id)] = tile[1:]
    return tiles


def tests():
    input = read_file("test_input.txt")
    assert part1(input) == 20899048083289


def get_tile_edges(tile: list) -> list:
    left = []
    right = []
    for i in tile:
        left.append(i[0])
        right.append(i[len(i) - 1])

    edges = []
    edges.append(tile[0])  # top
    edges.append("".join(right))  # right
    edges.append(tile[len(tile) - 1])  # bottom
    edges.append("".join(left))  # left
    return edges


def get_possible_neighbours(tile: int, edge: str, tiles: dict) -> list:
    possible_neighbours = []
    for t in tiles:
        if t != tile:
            for e in tiles[t]:
                if e == edge or e[::-1] == edge:
                    possible_neighbours.append(t)
    return possible_neighbours


def get_tiles_edges(input: dict) -> dict:
    tiles = {}
    for i in input:
        e = get_tile_edges(input[i])
        tiles[i] = e
    return tiles


def get_all_neighbours(tiles: dict) -> dict:
    all_neighbours = {}
    for i in tiles:
        neighbours = {}
        for e in tiles[i]:
            n = get_possible_neighbours(i, e, tiles)
            neighbours[e] = n
        all_neighbours[i] = neighbours
    return all_neighbours


def get_tiles_types(neighbours: dict) -> (list, list, list):
    corners = []
    edges = []
    rest = []
    for i in neighbours:
        empty_count = 0
        for n in neighbours[i]:
            if len(neighbours[i][n]) == 0:
                empty_count += 1

        if empty_count == 2:
            corners.append(i)
        elif empty_count == 1:
            edges.append(i)
        else:
            rest.append(i)

    return corners, edges, rest


def part1(input: dict) -> int:
    tiles = get_tiles_edges(input)
    neighbours = get_all_neighbours(tiles)
    corners, edges, rest = get_tiles_types(neighbours)

    product = 1
    for c in corners:
        product *= c
    return product


def part2(input: list) -> int:
    pass


if __name__ == "__main__":
    tests()
    input = read_file("input.txt")
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
