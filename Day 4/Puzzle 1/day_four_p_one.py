import copy


def get_paper_rolls(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        paper_grid = []
        for line in lines:
            line = line.strip()
            paper_grid.append(line)
    final = []
    for row in paper_grid:
        row_list = list(row)
        final.append(row_list)

    return final


def print_grid(paper_rolls_grid):
    for row in paper_rolls_grid:
        print(row)


def valid_paper_rolls(grid_o):
    grid = copy.deepcopy(grid_o)
    row_len = len(grid)
    column_len = len(grid[0])
    # print(row_len, column_len)
    new_grid = copy.deepcopy(grid)
    for row in range(row_len):
        for col in range(column_len):
            # print(grid[row][col])
            if grid[row][col] == '.':
                continue
            if grid[row][col] == '@':
                roll_count = -1
                for r in range(-1, 2):
                    for c in range(-1, 2):
                        if 0 <= row + r < row_len and 0 <= col + c < column_len:
                            if grid[row + r][col + c] == '@':
                                roll_count += 1
                if roll_count < 4:
                    new_grid[row][col] = 'x'
    return new_grid


def count_x(paper_rolls_grid):
    row_len = len(paper_rolls_grid)
    column_len = len(paper_rolls_grid[0])
    x_counter = 0
    for row in range(row_len):
        for col in range(column_len):
            if paper_rolls_grid[row][col] == 'x':
                x_counter += 1
    return x_counter


def main():
    paper_rolls = get_paper_rolls('paper_rolls.txt')
    # print_grid(valid_paper_rolls(paper_rolls))
    print(count_x(valid_paper_rolls(paper_rolls)))


if __name__ == '__main__':
    main()
