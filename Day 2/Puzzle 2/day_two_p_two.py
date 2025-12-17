def get_product_ids(filename):
    with open(filename, 'r') as file:
        return file.read().split(',')


def validate_ranges(product_id_ranges):
    invalid_id_list = []
    for product_id_range in product_id_ranges:
        invalid_id_list.extend(check_id_range(product_id_range))
    return invalid_id_list


def check_id_range(product_id_range):
    invalid_id_list = []
    id_range = product_id_range.split('-')
    begin, end = int(id_range[0]), int(id_range[1])
    for product_id in range(begin, end + 1):
        if check_valid_id(product_id):
            invalid_id_list.append(product_id)
    return invalid_id_list


def check_valid_id(product_id):
    product_id = str(product_id)
    product_id_length = len(product_id)

    valid_check = False
    if product_id[0] == '0' or product_id_length <= 1:  # starts with a leading zero -> invalid
        return False

    max_repeat_sizes = set((i + 1) // 2 for i in range(1, product_id_length + 1))

    for repeat_size in max_repeat_sizes:

        base_indices = list(range(0, product_id_length, repeat_size))
        valid_counter = 0

        for index in range(0, repeat_size):
            indices = [index + i for i in base_indices]

            # Check if any index equals product_id_length
            if any(i >= product_id_length for i in indices):
                valid_counter = 0
            # Check if all values at these indices are the same
            values_at_indices = [product_id[i] for i in indices if i < product_id_length]

            if len(set(values_at_indices)) == 1:  # All values are the same
                # All values at these indices are the same
                valid_counter += 1
        if valid_counter == repeat_size:
            valid_check = True

    return valid_check


def check_valid_id_ai(product_id):
    product_id = str(product_id)
    product_id_length = len(product_id)

    # Early return for invalid cases
    if product_id[0] == '0' or product_id_length <= 1:
        return False

    possible_repeat_sizes = set((i + 1) // 2 for i in range(1, product_id_length + 1))

    for repeat_size in possible_repeat_sizes:
        base_indices = list(range(0, product_id_length, repeat_size))
        valid_counter = 0

        for index in range(0, repeat_size):
            indices = [index + i for i in base_indices]

            # Check if any index is out of bounds (>= product_id_length)
            if any(i >= product_id_length for i in indices):
                # Skip this iteration - invalid index found
                continue

            # Check if all values at these indices are the same
            values_at_indices = [product_id[i] for i in indices]

            if len(set(values_at_indices)) == 1 and len(values_at_indices) > 0:
                valid_counter += 1

        # Early return if we found a valid pattern
        if valid_counter == repeat_size:
            return True

    return False


def sum_invalid_ids(invalid_id_list):
    invalid_id_sum = 0
    for invalid_id in invalid_id_list:
        invalid_id_sum += int(invalid_id)
    return invalid_id_sum


def main():
    product_id_ranges = get_product_ids('./Day 2/Puzzle 2/banks_samp.txt')
    invalid_id_list = validate_ranges(product_id_ranges)
    print(sum_invalid_ids(invalid_id_list))
    # print(invalid_id_list)


if __name__ == "__main__":
    main()
