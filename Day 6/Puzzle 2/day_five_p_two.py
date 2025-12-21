def get_ingredients(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        ingredient_id_ranges = []
        available_ingredient_ids = []
        for line in lines:
            if '-' in line:
                line = line.strip().split('-')
                tuple_id_range = (int(line[0]), int(line[1]))
                ingredient_id_ranges.append(tuple_id_range)
            elif line.strip() == '':
                continue
            else:
                line = line.strip()
                available_ingredient_ids.append(int(line))
    return ingredient_id_ranges, available_ingredient_ids


def merge_overlapping_ranges(ingredient_id_ranges):
    """
    Merge overlapping ranges efficiently.
    Algorithm: Sort by start, then merge overlapping/adjacent ranges.
    """
    if not ingredient_id_ranges:
        return []

    # Sort ranges by start value
    sorted_ranges = sorted(ingredient_id_ranges, key=lambda x: x[0])

    merged = [sorted_ranges[0]]

    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]

        # If current range overlaps or is adjacent to the last merged range
        if current_start <= last_end + 1:  # +1 for adjacent ranges (e.g., 5-6 and 7-8 merge to 5-8)
            # Merge: extend the end if current range extends further
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            # No overlap, add as new range
            merged.append((current_start, current_end))

    return merged


def validate_freshness(ing_ranges):
    count = 0
    for ing_id_ran in ing_ranges:
        count += ing_id_ran[1] - ing_id_ran[0] + 1
    return count


def main():
    ingredients = get_ingredients('ingredient_db.txt')
    ingredient_id_ranges, available_ingredient_ids = ingredients[0], ingredients[1]
    # print(ingredient_id_ranges)
    # print(available_ingredient_ids)
    optimized = merge_overlapping_ranges(ingredient_id_ranges)
    # print(optimized)
    print(validate_freshness(optimized))


if __name__ == '__main__':
    main()
