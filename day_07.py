def read_input(file):
    grid = [r.split("\n")[0] for r in open(file).readlines()]
    return grid


def process(grid):
    beam_split_counter = 0
    beam_locations = [0] * len(grid[0])
    beam_locations[grid[0].index("S")] = 1
    beam_locations_hist = [tuple(beam_locations)]
    for row in grid[1:]:
        if "^" not in row:
            continue
        else:
            for ix, c in enumerate(row):
                if c == "^" and beam_locations[ix] > 0:
                    stream_count = beam_locations[ix]
                    beam_split_counter += 1
                    beam_locations[ix] = 0
                    if ix > 0:
                        beam_locations[ix - 1] += stream_count
                    if ix < len(row):
                        beam_locations[ix + 1] += stream_count
        beam_locations_hist.append(tuple(beam_locations))
    print(f"Beam Splits are [{beam_split_counter}]")
    print(f"Streams per row are {[sum(i) for i in beam_locations_hist]}")


def main():
    # file = "./puzzle_inputs/day_07_sample.txt"
    file = "./puzzle_inputs/day_07_input.txt"

    grid = read_input(file)
    process(grid)
    print("Done")


if __name__ == "__main__":
    main()
