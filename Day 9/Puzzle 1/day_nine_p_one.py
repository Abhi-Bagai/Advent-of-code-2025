import copy


def get_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        input_values = [line.strip() for line in lines]
        coordinates = []
        for line in input_values:
            line = line.split(',')
            coord = map(int, line)
            coordinates.append(tuple(coord))
        return coordinates, len(coordinates) + 1


def display_grid(coordinates, height=9, width=14):  # (0, 0) is top right
    grid = []
    for y in range(height):
        row = ''
        for x in range(width):
            point = '.'
            if (x, y) in coordinates:
                point = '#'
            row += ' ' + point + ' '
        grid.append(row)
    for row in grid:
        print(row)
    return grid


def calculate_area(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def get_max_area(coordinates):
    coords = copy.copy(coordinates)
    max_area = 0
    for p1 in range(len(coords)):
        for p2 in range(p1, len(coords)):
            area = calculate_area(coords[p1], coords[p2])
            if area > max_area:
                max_area = area
    return max_area


def main():
    coordinates, height = get_input('./input.txt')
    print(height)
    # display_grid(coordinates)
    # print(calculate_area(coordinates[0], coordinates[2]))
    areas = get_max_area(coordinates)
    print(areas)


if __name__ == '__main__':
    main()
