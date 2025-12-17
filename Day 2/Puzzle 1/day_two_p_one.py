def get_product_ids():
    with open('product_ids.txt', 'r') as file:
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
        if not check_valid_id(product_id):
            invalid_id_list.append(product_id)
    return invalid_id_list


def check_valid_id(product_id):
    product_id = str(product_id)
    product_id_length = len(product_id)
    # print(product_id_length)
    max_repeat_size = product_id_length // 2
    repeat_count = 0
    if product_id[0] == '0':  # starts with a leading zero -> invalid
        return False
    if product_id_length % 2 == 1:  # has an odd length -> cannot be invalid
        return True
    for index in range(max_repeat_size):
        if product_id[index] == product_id[index + max_repeat_size]:
            repeat_count += 1
    if repeat_count == max_repeat_size:
        return False
    else:
        return True


def sum_invalid_ids(invalid_id_list):
    invalid_id_sum = 0
    for invalid_id in invalid_id_list:
        invalid_id_sum += int(invalid_id)
    return invalid_id_sum


def main():
    product_id_ranges = get_product_ids()
    invalid_id_list = validate_ranges(product_id_ranges)
    print(invalid_id_list)
    print(sum_invalid_ids(invalid_id_list))


if __name__ == "__main__":
    main()
