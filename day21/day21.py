import collections


def read_file(file: str) -> list:
    with open(file) as fp:
        input = []
        line = fp.readline().rstrip(")\n")
        while line:
            ingredients, allergens = line.split(" (contains ")
            ingredients = ingredients.split(" ")
            allergens = allergens.split(", ")
            record = {"ingredients": ingredients, "allergens": allergens}
            input.append(record)
            line = fp.readline().rstrip(")\n")
    return input


def tests():
    input = read_file("test_input.txt")
    assert part1(input) == 5
    assert part2(input) == 'mxmxvkd,sqjhc,fvjkl'


def get_allergens(input: list) -> dict:
    allergens = collections.defaultdict(set)
    for i, record in enumerate(input):
        for allergen in record["allergens"]:
            allergens[allergen].add(i)
    return allergens


def get_ingredients(input: list) -> dict:
    ingredients = collections.defaultdict(set)
    for i, record in enumerate(input):
        for ingredient in record["ingredients"]:
            ingredients[ingredient].add(i)
    return ingredients


def get_ingredients_without_allergens(input: list) -> list:
    allergens = get_allergens(input)
    ingredients = get_ingredients(input)

    without_allergens = []

    for i in ingredients:
        has_allergens = False
        for a in allergens:
            if allergens[a].issubset(ingredients[i]):
                has_allergens = True
        if not has_allergens:
            without_allergens.append(i)
    return without_allergens


def pair_ingredients_and_allergens(ingredients: dict, allergens: dict) -> dict:
    can_be_in_ingredients = collections.defaultdict(set)
    for a in allergens:
        for i in ingredients:
            if allergens[a].issubset(ingredients[i]):
                can_be_in_ingredients[a].add(i)

    pairs = {}
    while len(can_be_in_ingredients) > 0:
        allergens = can_be_in_ingredients.keys()
        paired = []
        # pair allergens with only one option
        for a in allergens:
            if len(can_be_in_ingredients[a]) == 1:
                ingredient = can_be_in_ingredients[a].pop()
                pairs[a] = ingredient
                paired.append(ingredient)

        for i in can_be_in_ingredients:
            # remove paired ingredients
            for p in paired:
                try:
                    can_be_in_ingredients[i].remove(p)
                except KeyError:
                    pass  # not present

        # remove paired allergens
        can_be_in_ingredients = {a: i for a, i in can_be_in_ingredients.items() if len(i) > 0}
    return pairs


def part1(input: list) -> int:
    all_ingredients = get_ingredients(input)
    without_allergens = get_ingredients_without_allergens(input)

    count = 0
    for i in without_allergens:
        count += len(all_ingredients[i])
    return count


def part2(input: list) -> str:
    ingredients = get_ingredients(input)
    allergens = get_allergens(input)
    ingredients_without_allergens = get_ingredients_without_allergens(input)

    # remove ingredients without allergens
    for wa in ingredients_without_allergens:
        del ingredients[wa]

    pairs = pair_ingredients_and_allergens(ingredients, allergens)

    result = []
    for i in dict(sorted(pairs.items())):
        result.append(pairs[i])
    return ",".join(result)


if __name__ == "__main__":
    tests()
    input = read_file("input.txt")
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
