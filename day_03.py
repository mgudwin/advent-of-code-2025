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


def process_old(banks, desired_length):
    ans = []
    for bank in banks:
        keep = []
        subset = bank[0 : -desired_length + 1]
        subset_max = max(subset)
        ix = subset.index(subset_max)
        keep = [subset[ix]]
        subset = bank[ix + 1 : desired_length + ix + 1]
        remaining = bank[desired_length + ix + 1 :]
        num_remaining = len(remaining)
        len_keep = len(keep)
        while num_remaining > 0:
            if subset[0] > subset[1]:
                if len_keep < desired_length:
                    keep.append(subset.pop(0))
                    subset.append(remaining.pop(0))
                else:
                    if keep[-1] < subset[0]:
                        keep.pop(-1)
                        keep.append(subset.pop(0))
                        subset.append(remaining.pop(0))
                    else:
                        subset.pop(0)
                        subset.append(remaining.pop(0))
            elif subset[0] == subset[1]:
                if len_keep < desired_length:
                    keep.append(subset.pop(0))
                    subset.append(remaining.pop(0))
                else:
                    subset.pop(0)
                    subset.append(remaining.pop(0))
            num_remaining = len(remaining)
            len_keep = len(keep)
        while len(subset) > 0:
            if keep[-1] < subset[0]:
                keep.pop(-1)
                keep.append(subset.pop(0))
            else:
                subset.pop(0)

        # while num_remaining > 0:
        #     subset_min = min(subset)
        #     min_ix = subset.index(subset_min)
        #     subset.pop(min_ix)
        #     subset.append(remaining.pop(0))
        #     num_remaining = len(remaining)
        # subset_min = min(subset)
        # min_ix = subset.index(subset_min)
        # subset.pop(min_ix)
        # keep += subset
        ans.append(keep)
    values = []
    for an in ans:
        value = 0
        for ix, digit in enumerate(an):
            value += digit * (10 ** (desired_length - 1 - ix))
        values.append(value)
    print(f"Total sum is {sum(values)}")


def main():
    file = "./puzzle_inputs/day_03_input.txt"
    # file = "./puzzle_inputs/day_03_sample.txt"
    banks = get_banks(file)
    new(banks, 12)


if __name__ == "__main__":
    main()
