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
    # print(banks)
    for bank in banks:
        joltage_tup = get_bank_joltage(bank, 12, joltage=[])
        total_joltage += concatenate_joltages(joltage_tup)
        # print('total_joltage: ', total_joltage)
    return total_joltage


def get_bank_joltage(bank, min_jolts, joltage):
    bank_length = len(bank)
    # print('bank: ', bank, ', bank_length', bank_length, ' min_jolts: ', min_jolts, ', joltage: ', joltage)
    if len(joltage) == 12:
        return joltage, ''
    elif bank_length + len(joltage) == 12:
        return joltage, bank

    max_joltage = 0
    indices = [i for i in range(0, bank_length - min_jolts + 1)]
    # print('indices', indices)
    new_start = 0
    for i in indices:
        if int(bank[i]) > max_joltage:
            max_joltage = int(bank[i])
            new_start = i + 1
    joltage.append(max_joltage)
    # print('joltage: ', joltage, ', new_start: ', new_start, ', min_jolts: ', min_jolts)
    return get_bank_joltage(bank[new_start:], min_jolts - 1, joltage)


def concatenate_joltages(jolt_plus):
    jolt = jolt_plus[0]
    suffix = str(jolt_plus[1])
    prefix = ''
    for jolt in jolt:
        prefix += str(jolt)
    total = prefix + suffix
    return int(total)


def main():
    print(get_total_joltages(get_banks('banks.txt')))


if __name__ == "__main__":
    main()
