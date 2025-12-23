def get_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        input_values = [line.strip() for line in lines]
        return input_values, len(input_values), len(input_values[0])


def split_beam_and_count(input_values, width):
    split_count = 0
    first_line = input_values[0]
    current_ind = [i for i in range(width) if first_line[i] == 'S']
    for line in input_values[1:]:
        for pi in range(width):
            if line[pi] == '^' and pi in current_ind:
                split_count += 1
                current_ind.remove(pi)
                current_ind.append(pi + 1)
                current_ind.append(pi - 1)
                current_ind = list(set(current_ind))

        # print(line, current_ind)
    current_ind = list(set(current_ind))
    return split_count, current_ind


def main():
    input_values, height, width = get_input('input.txt')
    # print(input_values, '\n', height, '\n', width)
    results = split_beam_and_count(input_values, width)
    print(results[0])
    print(results[1])


if __name__ == '__main__':
    main()
