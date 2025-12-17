def get_banks(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        banks = []
        for line in lines:
            line = line.strip()
            banks.append(line)
    return banks


def get_total_joltages(banks):
    total_joltage = 0
    for bank in banks:
        total_joltage += get_bank_joltage(bank)
        # print(get_bank_joltage(bank))
    return total_joltage


def get_bank_joltage(bank_str):
    bank_length = len(bank_str)
    max_joltage_tens = -1
    tens_index = 0
    for bat in range(bank_length - 1):
        if int(bank_str[bat]) > max_joltage_tens:
            max_joltage_tens = int(bank_str[bat])
            # print(max_joltage_tens)
            tens_index = bat
            # print(tens_index)
    max_joltage_ones = -1
    # ones_index = tens_index + 1
    for bat in range(bank_length - 1, tens_index, -1):
        if int(bank_str[bat]) > max_joltage_ones:
            max_joltage_ones = int(bank_str[bat])
            # ones_index = bat

    return max_joltage_tens * 10 + max_joltage_ones


def main():
    print(get_total_joltages(get_banks('banks.txt')))
    # print(get_bank_joltage('987654321111111'))


if __name__ == "__main__":
    main()
