# import numpy as np

def get_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        input_values = []

        for line in lines:
            str_line = line.split(' ')
            input_values.append(str_line)

    operators = input_values[-1]
    input_values = input_values[:-1]
    return input_values, operators


def clean_up_num(lines):
    input_values = []
    for line in lines:
        new_line = []
        for num in line:
            num = num.strip()
            if num == '':
                continue
            new_line.append(int(num))
        input_values.append(new_line)
    return input_values


def clean_up_op(line):
    operators = []
    for op in line:
        op = op.strip()
        if op == '':
            continue
        operators.append(op)
    return operators


def transpose_input(input_values):
    transposed = [
        [row[i] for row in input_values]
        for i in range(len(input_values[0]))
    ]
    return transposed


def calculate_total(inputs, operators):
    total = 0
    for row in range(len(inputs)):
        if operators[row] == '+':
            total += add_row(inputs[row])
        if operators[row] == '*':
            total += multiply_row(inputs[row])
    return total


def add_row(row):
    total = 0
    for num in row:
        total += num
    return total


def multiply_row(row):
    total = 1
    for num in row:
        total *= num
    return total


def main():
    input_values, operators = get_input('input.txt')
    input_values = clean_up_num(input_values)
    operators = clean_up_op(operators)
    transposed = transpose_input(input_values)
    # print(input_values, operators)
    # print(transposed)
    # transposed2 = np.array(input_values).T
    # print(transposed2)
    print(calculate_total(transposed, operators))


if __name__ == '__main__':
    main()
