def get_rotations():
    rotations = []
    with open('rotations.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            rotations.append(line)
    return rotations


def get_position(rotations):
    zero_counter = 0
    position = 50
    for rotation in rotations:
        if rotation[0] == 'L':
            r_value = int(rotation[1:]) % 100
            position = position - r_value
            if position < 0:
                position = position + 100  # if the position is negative, add 100 to it
        elif rotation[0] == 'R':
            r_value = int(rotation[1:]) % 100
            position = position + r_value
            if position > 99:
                position = position - 100
        if position == 0:
            zero_counter += 1
    return zero_counter


def main():
    print("Zero counter: ", get_position(get_rotations()))


if __name__ == "__main__":
    main()
