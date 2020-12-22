def read_file(file: str) -> (list, list):
    with open(file) as fp:
        fp.readline().rstrip(")\n")  # Player 1
        player1 = []

        line = fp.readline().rstrip(")\n")
        while line:
            player1.append(int(line))
            line = fp.readline().rstrip(")\n")

        fp.readline().rstrip(")\n")  # Player 2
        player2 = []
        line = fp.readline().rstrip(")\n")
        while line:
            player2.append(int(line))
            line = fp.readline().rstrip(")\n")
    return player1, player2


def tests():
    player1, player2 = read_file("test_input.txt")
    assert part1(player1, player2) == 306
    assert part2(player1, player2) == 291


def calculate_score(winner_deck: list) -> int:
    score = 0
    for i, item in enumerate(winner_deck[::-1]):
        score += item * (i + 1)
    return score


def play_combat(player1: list, player2: list) -> (int, list):
    while len(player1) > 0 and len(player2) > 0:
        p1 = player1.pop(0)
        p2 = player2.pop(0)

        if p1 > p2:
            # p1 wins
            player1.append(p1)
            player1.append(p2)
        else:
            # p2 wins
            player2.append(p2)
            player2.append(p1)

    # return winner and winner's deck
    if len(player1) == 0:
        return 1, player2
    else:
        return 0, player1


def play_recursive_combat(player1: list, player2: list) -> (int, list):
    previous_decks = set()
    while len(player1) > 0 and len(player2) > 0:
        if (tuple(player1), tuple(player2)) in previous_decks:
            return 1, player1

        previous_decks.add((tuple(player1), tuple(player2)))

        p1 = player1.pop(0)
        p2 = player2.pop(0)
        if len(player1) >= p1 and len(player2) >= p2:
            # sub-game
            winner, _ = play_recursive_combat(list(player1)[:p1], list(player2)[:p2])
        else:
            if p1 > p2:
                winner = 1
            else:
                winner = 2

        if winner == 1:
            player1.append(p1)
            player1.append(p2)
        else:
            player2.append(p2)
            player2.append(p1)

    # return winner and winner's deck
    if len(player1) == 0:
        return 2, player2
    else:
        return 1, player1


def part1(player1: list, player2: list) -> int:
    _, winner_deck = play_combat(list(player1), list(player2))
    return calculate_score(winner_deck)


def part2(player1: list, player2: list) -> int:
    _, winner_deck = play_recursive_combat(player1, player2)
    return calculate_score(winner_deck)


if __name__ == "__main__":
    tests()
    player1, player2 = read_file("input.txt")
    print(f"Part 1: {part1(player1, player2)}")
    print(f"Part 2: {part2(player1, player2)}")
