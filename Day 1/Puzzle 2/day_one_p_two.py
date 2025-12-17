def get_rotations():
    rotations = []
    with open('rotations.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            rotations.append(line)
    return rotations


def update_counter_and_position(rotations):
    zero_counter = 0
    position = 50
    for rotation in rotations:
        pos_and_counter = update_position(position, rotation)
        position = pos_and_counter[0]
        zero_counter += pos_and_counter[1]
    return zero_counter, position


def update_position(position, rotation):
    zero_counter = 0
    value = int(rotation[1:])
    if rotation[0] == 'L':
        for i in range(1, value + 1):
            position -= 1
            if position == 0:
                zero_counter += 1
            if position == -1:
                position = 99
    elif rotation[0] == 'R':
        for i in range(1, value + 1):
            position += 1
            if position == 100:
                position = 0
                zero_counter += 1
    return [position, zero_counter]


def main():
    print("Zero counter: ", update_counter_and_position(get_rotations()))


if __name__ == "__main__":
    main()
