

def get_change(input):
    input_direction = str(input[0])
    input_amount = int(input[1:])
    direction = 1
    if (input_direction == 'L') or (input_direction == 'R'):
        if input_direction == 'L':
            direction = -1
        elif input_direction == 'R':
            direction = 1
    else:
        print('DIRECTION ERROR')
    return direction * input_amount
        
def get_delta(current_position, changes):
    return (current_position + get_change(changes))

def calculate_position(dial, crossings=0):
    if (dial >= 0) and (dial <= 99):
        return dial, crossings
    elif dial > 99:
        dial -= 100
        if dial != 0:
            crossings += 1
        return calculate_position(dial, crossings)
    elif dial < 0:
        dial += 100
        if dial != 0:
            crossings += 1
        return calculate_position(dial, crossings)
    else:
        return 'ERROR'

def read_rotations(file):
    with open(file) as f:
        lines = [line.rstrip() for line in f]

    return lines

def main():
    counts = 0
    position = 50
    aim = 0
    positions = [position]

    rotations = read_rotations('puzzle_inputs/day_01_sample.txt')
    # rotations = read_rotations('puzzle_inputs/day_01_input.txt')
    print(f'The dial starts by pointing at {position}')

    for rotation in rotations:
        position, _counts = calculate_position(get_delta(position, rotation))
        counts += _counts
        print(f'The dial is rotated {rotation} to point at [{position}]; during this rotation, it points at {aim} [{counts}] times')
        positions.append(position)
    
    zero_positions = positions.count(0)
    total_zeros = counts + zero_positions

    print(f'Final is {position}')
    # print(f'All positions are:\n\t{positions}')
    print(f'Total number of {aim} is {zero_positions} and crosses {aim} {counts} times for a total of {total_zeros}')
    print('Done')

if __name__ == "__main__":
    main()