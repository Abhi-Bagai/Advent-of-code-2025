import copy


def get_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        input_values = [line.strip() for line in lines]
        coordinates = []
        max_val = 0
        min_value = 100000
        for line in input_values:
            line = line.split(',')
            coord = tuple(map(int, line))
            coordinates.append(coord)
            val_big = max(list(coord))
            val_small = min(list(coord))
            # print(coord, val_big)
            if val_big > max_val:
                max_val = val_big
            if val_small < min_value:
                min_value = val_small
        return coordinates, max_val + 2, min_value - 1


def display_grid(grid, size, minimum):  # (0, 0) is top right
    for y in range(minimum, size):
        row = []
        for x in range(minimum, size):
            row.append(grid[y][x])
        print(row)


def add_red_tiles(red_coords, size, minimum):
    grid = []
    for y in range(minimum, size):
        row = []
        for x in range(minimum, size):
            point = '.'
            if (x, y) in red_coords:
                point = '#'
            row += point
        grid.append(row)
    return grid


def get_green_coordinates(coordinates):
    red_coordinates = copy.deepcopy(coordinates)
    green_coordinates = []
    red_coord_original = red_coordinates[0]

    while len(red_coordinates) > 0:
        if len(red_coordinates) == 1:
            cx, cy = red_coordinates[0]
            nx, ny = red_coord_original
        else:
            cx, cy = red_coordinates[0]
            nx, ny = red_coordinates[1]

        # print(cx, cy, nx, ny)
        if cx == nx:
            if ny > cy:
                for i in range(cy + 1, ny):
                    green_coordinates.append((cx, i))
            else:
                for i in range(ny + 1, cy):
                    green_coordinates.append((cx, i))
        elif cy == ny:
            if nx > cx:
                for i in range(cx + 1, nx):
                    green_coordinates.append((i, cy))
            else:
                for i in range(nx + 1, cx):
                    green_coordinates.append((i, cy))

        red_coordinates.pop(0)
    # print(green_coordinates)
    return green_coordinates


def add_green_tiles(green_coordinates, size, minimum):
    grid = []
    for y in range(minimum, size):
        row = []
        for x in range(minimum, size):
            point = '.'
            if (x, y) in green_coordinates:
                point = 'X'
            row += point
        grid.append(row)
    return grid


def fill_green_coords(grid, green_coordinates, size, minimum):
    rows_add = []
    for row in range(minimum, size):
        if grid[row].count('X') >= 2:
            rows_add.append(row)
    # print(rows_add)
    while len(rows_add) > 0:
        rx = rows_add.pop(0)
        points = []
        for x, y in green_coordinates:
            if y == rx:
                points.append((x, y))
        points.sort(key=lambda point: point[0])
        for point in range(points[0][0], points[-1][0]):
            green_coordinates.append((point, rx))
    green_coordinates = list(set(green_coordinates))
    return green_coordinates


def grid_red_green(green, red, size, minimum):
    grid = []
    for y in range(minimum, size):
        row = []
        for x in range(minimum, size):
            point = '.'
            if (x, y) in green:
                point = 'X'
            elif (x, y) in red:
                point = '#'
            row += point
        grid.append(row)
    return grid


def calculate_area(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def get_bounding_box(point1, point2):
    bounding_box = []
    points = [point1, point2]
    points_x = sorted(points, key=lambda point: point[0])
    points_y = sorted(points, key=lambda point: point[1])
    # points_y = points.sort(key=lambda point: point[1])
    x1 = points_x[0][0]
    x2 = points_x[1][0]
    y1 = points_y[0][1]
    y2 = points_y[1][1]
    # print(x1, y1, x2, y2)
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            bounding_box.append((x, y))
    # print(f'bounding_box{bounding_box} length: {len(bounding_box)}')
    return bounding_box


def get_max_area(red_coords, all_coords):
    coords = copy.copy(red_coords)
    max_area = 0
    for p1 in range(len(coords)):
        for p2 in range(p1, len(coords)):
            bounding_box = get_bounding_box(coords[p1], coords[p2])
            count = 0
            for coord in bounding_box:
                if coord in all_coords:
                    count += 1
            if count == len(bounding_box):
                area = calculate_area(coords[p1], coords[p2])
                if area > max_area:
                    max_area = area
    return max_area


def main():
    red_coordinates, size, minimum = get_input('./input2.txt')
    print(red_coordinates, '\n', size, '\n', minimum)
    # grid_red = add_red_tiles(red_coordinates, size, minimum)
    # grid = add_green_tiles(coordinates, size)
    # print(grid_red)
    green_coords = get_green_coordinates(red_coordinates)
    # print(len(green_coords))
    grid_green = add_green_tiles(green_coords, size, minimum)
    green_coords = fill_green_coords(grid_green, green_coords, size, minimum)
    grid_green = add_green_tiles(green_coords, size, minimum)
    # print(len(green_coords))
    # display_grid(grid_green, size, minimum)
    red_green_coord = green_coords + red_coordinates
    red_green_coord = list(set(red_green_coord))
    grid_complete = grid_red_green(green_coords, red_coordinates, size, minimum)
    display_grid(grid_complete, size, minimum)
    max_area = get_max_area(red_coordinates, red_green_coord)
    print(max_area)


if __name__ == '__main__':
    main()
