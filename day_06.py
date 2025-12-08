def get_input(file):
    all = [r.split("\n")[0] for r in open(file).readlines()]
    all = [" ".join(row.split()).split() for row in all]
    return all


def get_input_part2(file):
    all = [r.split("\n")[0] for r in open(file).readlines()]
    all = [list(row) for row in all]
    all_numbers = all[:-1]
    operators = [op for op in all[-1] if op != " "]
    operators_in_order = operators[::-1]
    mutated_numbers = []
    for i in range(len(all_numbers[0]) - 1, -1, -1):
        t = "".join([row[i] for row in all_numbers])
        if t.count(" ") == len(t):
            mutated_numbers.append("|")
            continue
        _mutate = int(t)
        mutated_numbers.append(_mutate)
    total_numbers = []
    running = []
    for n in mutated_numbers:
        if n != "|":
            running.append(n)
        elif n == "|":
            total_numbers.append(running)
            running = []
    total_numbers.append(running)
    return total_numbers, operators_in_order


def part1(math_problem):
    total = 0
    for i in range(len(math_problem[0])):
        problem = [row[i] for row in math_problem]
        operator = problem[-1]
        problem_result = int(problem[0])
        for num in problem[1:-1]:
            if operator == "+":
                problem_result += int(num)
            elif operator == "*":
                problem_result *= int(num)
        total += problem_result
    return total


def main():
    # file = "./puzzle_inputs/day_06_sample.txt"
    file = "./puzzle_inputs/day_06_input.txt"

    math_problem = get_input(file)

    # Part 1
    total = part1(math_problem)
    print(f"Total for Part 1 is {total}")

    # Part 2
    numbers, operators = get_input_part2(file)
    total = 0
    if len(numbers) != len(operators):
        print(
            f"Uh On. Num of Problems {len(numbers)} != Num of Operators {len(operators)}"
        )
    else:
        print(
            f"Yay Num of Problems {len(numbers)} == Num of Operators {len(operators)}"
        )
    for ix, problem in enumerate(numbers):
        op = operators[ix]
        problem_total = problem[0]
        for c in problem[1:]:
            if op == "+":
                problem_total += c
            if op == "*":
                problem_total *= c
        total += problem_total

    print(f"Total for Part 2 is {total}")


if __name__ == "__main__":
    main()
