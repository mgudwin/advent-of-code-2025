def convert_rotation(input):
    """
    Get the change by converting L to - and R to +
    """
    input_direction = str(input[0])
    input_amount = int(input[1:])
    if input_direction == "L":
        return -1 * input_amount
    elif input_direction == "R":
        return input_amount


def get_dial_change(current_position, changes):
    """
    Find next value give current and change. Count 0 crossings
    """
    crossing_count = 0
    previous_position = current_position
    next_position = previous_position + convert_rotation(changes)
    rotations, remainder = divmod(next_position, 100)

    if rotations < 0:
        crossing_count += abs(rotations) - 1
    if rotations > 0:
        crossing_count += rotations
    if remainder == 0:
        if rotations < 0:
            crossing_count = abs(rotations) - 1
        if rotations > 0:
            crossing_count -= 1
    if (previous_position < 0) and (next_position > 0):
        crossing_count += 1
    if (previous_position > 0) and (next_position < 0):
        crossing_count += 1
    return remainder, crossing_count


def read_rotations(file):
    with open(file) as f:
        lines = [line.rstrip() for line in f]
    return lines


def main():
    crossing_counts = 0
    position = 50
    aim = 0
    positions = [position]

    # rotations = read_rotations("puzzle_inputs/day_01_sample.txt")
    rotations = read_rotations("puzzle_inputs/day_01_input.txt")
    print(f"The dial starts by pointing at {position}")

    for rotation in rotations:
        position, crossing = get_dial_change(position, rotation)
        crossing_counts += crossing
        print(
            f"The dial is rotated {rotation:>5} to point at [{position:>2}];"
            f" during this rotation, it points at {aim} [{crossing:>2}] times"
        )
        positions.append(position)

    zero_positions = positions.count(0)
    total_zeros = crossing_counts + zero_positions

    print(f"Final is {position}")
    print(
        f"Total number of {aim}'s found is [{zero_positions}] and crosses {aim}"
        f" [{crossing_counts}] times for a total of [{total_zeros}]"
    )
    print("Done")


if __name__ == "__main__":
    main()
