def part_1(ingredients, fresh):
    fresh_count = 0
    for ingredient in ingredients:
        for test in fresh:
            if ingredient in range(test[0], test[1] + 1):
                fresh_count += 1
                break
    print(f"Part 1 has [{fresh_count}] fresh ingredients")


def get_input(file):
    all = [r.split("\n")[0] for r in open(file).readlines()]
    fresh = tuple(
        sorted(
            tuple([tuple(map(int, f.split("-"))) for f in all[: all.index("")]]),
            key=lambda tup: tup[0],
        )
    )
    ingredients = tuple(map(int, [f for f in all[all.index("") + 1 :]]))
    return ingredients, fresh


def reduce(items):
    for i in range(len(items) - 1):
        min_0 = min(items[i])
        max_0 = max(items[i])
        min_1 = min(items[i + 1])
        max_1 = max(items[i + 1])
        if min_1 <= max_0:
            t = items[:i] + ((min_0, max(max_0, max_1)),) + items[i + 2 :]
            return t
            print("Combine!")
    return items


def check_overlap(items):
    for i in range(len(items) - 1):
        min_0 = min(items[i])
        max_0 = max(items[i])
        min_1 = min(items[i + 1])
        max_1 = max(items[i + 1])
        if min_1 <= max_0:
            return True
    return False


def main():
    # file = "./puzzle_inputs/day_05_sample.txt"
    file = "./puzzle_inputs/day_05_input.txt"

    ingredients, fresh = get_input(file)

    part_1(ingredients, fresh)

    # Part 2

    overlap = check_overlap(fresh)
    reduced = fresh
    while overlap:
        reduced = reduce(reduced)
        overlap = check_overlap(reduced)

    final = 0
    for item in reduced:
        _min = item[0]
        _max = item[1]
        final += _max - _min + 1

    print(f"Part 2 should have [{final}] total ingredients")


if __name__ == "__main__":
    main()
