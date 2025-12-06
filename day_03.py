def convert_to_int(list, desired_length):
    value = 0
    for ix, digit in enumerate(list):
        value += digit * (10 ** (desired_length - 1 - ix))
    return value


def process_banks(banks, desired_length):
    ans = []
    for bank in banks:
        keep = []
        subset = bank[0 : -desired_length + 1]
        subset_max = max(subset)
        ix = subset.index(subset_max)
        keep.append(subset.pop(ix))
        subset = bank[ix + 1 :]
        final = process_bank(subset, desired_length, keep)
        joltage = convert_to_int(final, desired_length)
        ans.append(joltage)
    print(f"Joltage total:\t{sum(ans)}")
    print("done")


def process_bank(subset, desired_length, keep=[]):
    reserved_range = desired_length - len(keep)
    # If there's only one more value to add
    if reserved_range == 1:
        keep.append(subset.pop(0))
        return process_bank(subset, desired_length, keep)
    # If more than 1 value needs to be added
    if len(keep) < desired_length:
        search = subset[0 : -reserved_range + 1]
        subset_max = max(search)
        ix = subset.index(subset_max)
        keep.append(subset[ix])
        subset = subset[ix + 1 :]
        return process_bank(subset, desired_length, keep)
    # If in the reserve pool
    if len(keep) == desired_length and len(subset) > 0:
        keep_last = keep[-1]
        subset_first = subset[0]
        if keep_last < subset_first:
            keep.pop(-1)
            keep.append(subset.pop(0))
        elif keep_last >= subset_first:
            subset.pop(0)
        return process_bank(subset, desired_length, keep)
    return keep


def main():
    file = "./puzzle_inputs/day_03_input.txt"
    # file = "./puzzle_inputs/day_03_sample.txt"

    banks = [r.split("\n")[0] for r in open(file).readlines()]
    banks = [[int(x) for x in bank] for bank in banks]
    process_banks(banks, 12)


if __name__ == "__main__":
    main()
