class Map:
    def __init__(self, _file):
        self.rows = [r.split("\n")[0] for r in open(_file).readlines()]
        self.rows = [list(row) for row in self.rows]
        num_columns = len(self.rows[0])
        num_rows = len([row[0] for row in self.rows])
        self.shape = (num_rows, num_columns)
        self.accessible_rolls = []

    def print_map(self):
        [print("".join(row)) for row in self.rows]

    def get_neighbors(self, r, c, max_row, max_col):
        neighbors = []
        for cell in [
            [r - 1, c - 1],
            [r - 1, c],
            [r - 1, c + 1],
            [r, c - 1],
            [r, c + 1],
            [r + 1, c - 1],
            [r + 1, c],
            [r + 1, c + 1],
        ]:
            neighbors.append(cell)
        # Clean neighbors
        neighbors = [
            neighbor
            for neighbor in neighbors
            if (
                (
                    neighbor[0] in range(0, max_row)
                    and (neighbor[1] in range(0, max_col))
                )
            )
        ]

        return neighbors

    def count_rolls(self):
        self.count_of_rolls = {}
        for r in range(0, self.shape[0]):
            for c in range(0, self.shape[1]):
                count = 0
                if self.rows[r][c] != "@":
                    continue
                for cell in self.get_neighbors(r, c, self.shape[0], self.shape[1]):
                    test_value = self.rows[cell[0]][cell[1]]
                    if test_value == "@":
                        count += 1
                # self.count_of_rolls["".join([str(r), str(c)])] = count
                self.count_of_rolls[(r, c)] = count

    def count_of_rolls_with_lt(self, count):
        for key, value in self.count_of_rolls.items():
            if value < count:
                self.accessible_rolls.append(key)
        self.removable_rolls = len(self.accessible_rolls)
        print(f"There are {self.removable_rolls} accessible rolls!")

    def remove_rolls(self, count):
        for key, value in self.count_of_rolls.items():
            if value < count:
                self.rows[key[0]][key[1]] = "."


def main():
    file = "./puzzle_inputs/day_04_input.txt"
    # file = "./puzzle_inputs/day_04_sample.txt"
    grid = Map(file)
    grid.count_rolls()
    grid.count_of_rolls_with_lt(4)
    grid.remove_rolls(4)
    runs = 1
    while runs < 50:
        i = grid.removable_rolls
        grid.count_rolls()
        grid.count_of_rolls_with_lt(4)
        grid.remove_rolls(4)

    grid.print_map()
    print("yay")


# [00][01][02][03]
# [10][11][12][13]
# [20][21][22][23]
# so for rc, list is (r-1, c-1), (r-1, c), (r-1, c+1),
#                    (r  , c-1), (r  , c), (r  , c+1),
#                    (r+1, c-1), (r+1, c), (r+1, c+1)

if __name__ == "__main__":
    main()
