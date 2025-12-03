def get_banks(file):
    banks = [r.split("\n")[0] for r in open(file).readlines()]

    banks = [[int(x) for x in bank] for bank in banks]
    return banks


def part1(banks):
    bank_max = []

    for r, bank in enumerate(banks):
        joltage = {}

        for tix, tens in enumerate(bank):
            tens_seen = []
            if tens in tens_seen:
                continue
            else:
                tens_seen.append(tens)

            for oix, ones in enumerate(bank):
                if oix <= tix:
                    continue
                ones_seen = []
                if ones in ones_seen:
                    continue
                else:
                    ones_seen.append(ones)
                joltage[(tens * 10) + ones] = [tix, oix]

        max_joltage = max(list(joltage.keys()))
        bank_max.append(max_joltage)

    sum_of_max = sum(bank_max)
    print(f"Part 1 solution is {sum_of_max}")


def main():
    file = "./puzzle_inputs/day_03_input.txt"
    # file = "./puzzle_inputs/day_03_sample.txt"
    banks = get_banks(file)
    part1(banks)


if __name__ == "__main__":
    main()
