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

    return final, 0


def print_grid(paper_rolls_grid):
    grid = paper_rolls_grid[0]
    print(paper_rolls_grid[1])
    for row in grid:
        print(row)


def remove_paper_rolls(grid_o):
    grid_tup = copy.deepcopy(grid_o)
    grid = grid_tup[0]
    row_len = len(grid)
    column_len = len(grid[0])
    # print(row_len, column_len)
    new_grid = copy.deepcopy(grid)
    total_removed = 0
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
                    new_grid[row][col] = '.'
                    # new_grid[row][col] = 'x'
                    total_removed += 1
    return new_grid, total_removed


def get_total_removed(paper_rolls_grid_tup):
    paper_rolls_grid = paper_rolls_grid_tup[0]
    total_removed = paper_rolls_grid_tup[1]
    grid_tup_copy = copy.deepcopy(paper_rolls_grid_tup)
    # print_grid(paper_rolls_grid_tup)
    while True:
        removed = remove_paper_rolls(grid_tup_copy)
        total_removed += removed[1]
        grid_tup_copy = removed
        if removed[1] == 0:
            print("total: ", total_removed)
            break
    return paper_rolls_grid, total_removed


def main():
    paper_rolls = get_paper_rolls('../Puzzle 1/paper_rolls.txt')
    # paper_rolls = get_paper_rolls('../Puzzle 1/sample.txt')

    print(get_total_removed(paper_rolls)[1])



if __name__ == '__main__':
    main()
