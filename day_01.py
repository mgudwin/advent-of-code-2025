

def convert_rotation(input):
    '''
    Get the change by converting L to - and R to +
    '''
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
        
def get_dial_change(current_position, changes):
    '''
    Find next value give current and change. Count 0 crossings
    '''
    crossing_count = 0
    previous_position = current_position
    current_position = previous_position + int(convert_rotation(changes))
    times = int(abs(current_position/100))
    if (previous_position < 0) and (current_position > 0):
        if abs(current_position > 100):
            crossing_count += (1 * times)
        else:
            crossing_count += 1
    elif (previous_position > 0) and (current_position < 0):
        if abs(current_position > 100):
            crossing_count += (1 * times)
        else:
            crossing_count += 1
    elif abs(current_position) > 100:
            crossing_count += (1 * times)
    return current_position, crossing_count

def calculate_dial_position(dial):
    '''
    Get final dial position after change
    '''
    if dial > 99:
        dial -= 100
        return calculate_dial_position(dial)
    elif dial < 0:
        dial += 100
        return calculate_dial_position(dial)
    else:
        return dial
    
def read_rotations(file):
    with open(file) as f:
        lines = [line.rstrip() for line in f]

    return lines

def main():
    crossing_counts = 0
    position = 50
    aim = 0
    positions = [position]

    rotations = read_rotations('puzzle_inputs/day_01_sample.txt')
    # rotations = read_rotations('puzzle_inputs/day_01_input.txt')
    print(f'The dial starts by pointing at {position}')

    for rotation in rotations:
        delta, crossing = get_dial_change(position, rotation)
        position = calculate_dial_position(delta)
        if crossing > 0:
            crossing_counts += crossing
            print(f'The dial is rotated {rotation} to point at [{position}]; during this rotation, it points at {aim} [{crossing}] times')
        else:
            print(f'The dial is rotated {rotation} to point at [{position}].')
        positions.append(position)
    
    zero_positions = positions.count(0)
    total_zeros = crossing_counts + zero_positions

    print(f'Final is {position}')
    print(f'Total number of {aim} is {zero_positions} and crosses {aim} {crossing_counts} times for a total of {total_zeros}')
    print('Done')

if __name__ == "__main__":
    main()