def get_banks(file):
    banks = [r.split("\n")[0] for r in open(file).readlines()]

    banks = [[int(x) for x in bank] for bank in banks]
    return banks


def convert_to_int(list, desired_length):
    value = 0
    for ix, digit in enumerate(list):
        value += digit * (10 ** (desired_length - 1 - ix))
    return value


def remove_bads(subset, ix, desired_length):
    subset_length = len(subset)
    if subset_length > desired_length:
        min_subset = min(subset)
        min_ix = subset.index(min_subset)
        subset.pop(min_ix)
        return remove_bads(subset, ix, desired_length)
    return subset


def new(banks, desired_length):
    ans = []
    for bank in banks:
        keep = []
        subset = bank[0 : -desired_length + 1]
        subset_max = max(subset)
        ix = subset.index(subset_max)
        subset = bank[ix:]
        subset = remove_bads(subset, 1, desired_length)
        joltage = convert_to_int(subset, desired_length)
        ans.append(joltage)
    print(f"Joltages are:\n{ans}")
    print(f"Joltage total:\t{sum(ans)}")
    print("done")


def main():
    file = "./puzzle_inputs/day_03_input.txt"
    # file = "./puzzle_inputs/day_03_sample.txt"
    banks = get_banks(file)
    new(banks, 12)


if __name__ == "__main__":
    main()
