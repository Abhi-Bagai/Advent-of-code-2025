# import numpy as np

def get_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        input_values = []
        operators = lines[-1]
        max_line_length = max([len(line) for line in lines])
        max_line_length = max_line_length - 1
        for line in lines[:-1]:
            line = line[:-1]
            if len(line) < max_line_length:
                add = max_line_length - len(line)
                line = line + ' ' * add
            input_values.append(line)

        if len(operators) < max_line_length:
            add = max_line_length - len(operators)
            operators = operators + ' ' * add

    return input_values, operators


def clean_up_num(lines):
    input_values = []
    for line in lines:
        new_line = [i for i in line]
        input_values.append(new_line)
    return input_values


def clean_up_op(line):
    operators = []
    for i in line:
        if i != ' ':
            operators.append(i)

    return operators


def transpose_input(input_values):
    transposed = [
        [row[i] for row in input_values]
        for i in range(len(input_values[0]))
    ]
    return transposed


def transform_input(input_values):
    transposed = transpose_input(input_values)
    transformed = []
    for i in range(len(transposed)):
        if transposed[i] != [' ', ' ', ' ']:  # remove [' ', ' ', ' ']
            transformed.append(transposed[i])
    for i_list in transformed:
        # print(i_list)
        for j_str in range(len(i_list)):
            if i_list[j_str] == ' ':
                i_list[j_str] = '0'
        # print(i_list)
    remove_zeros = []
    for seq in transformed:
        seq_str = ''
        for i in range(len(seq)):
            seq[i] = int(seq[i])
            if seq[i] > 0:
                seq_str += str(seq[i])
        remove_zeros.append(seq_str.strip())
    # print(remove_zeros)
    input_ints = remove_zeros
    # input_ints = [int(i) for i in remove_zeros if i != '']
    # print('start ', input_ints)

    input_ints_seg = []
    while len(input_ints) > 0:
        segment = []
        while len(input_ints) > 0 and input_ints[0] != '':
            segment.append(input_ints[0])
            input_ints.pop(0)

        input_ints_seg.append(segment)
        if len(input_ints) > 0:
            input_ints.pop(0)

    # print('this', input_ints_seg)

    return input_ints_seg


def calculate_total(inputs, operators):
    total = 0
    for item in zip(inputs, operators):
        if item[1] == '+':
            total += add_row(item[0])
        elif item[1] == '*':
            total += multiply_row(item[0])
    return total


def add_row(row):
    row = [int(num) for num in row]
    # print('row', row)
    total = 0
    for num in row:
        total += num
    return total


def multiply_row(row):
    row = [int(num) for num in row]
    # print('row', row)
    total = 1
    for num in row:
        total *= num
    return total


def main():
    input_values, operators = get_input('input.txt')
    input_values = clean_up_num(input_values)
    input_values = transform_input(input_values)

    operators = clean_up_op(operators)

    print(calculate_total(input_values, operators))


if __name__ == '__main__':
    main()
