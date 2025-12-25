from math import sqrt


def get_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        input_values = [line.strip().split(',') for line in lines]
        results = []
        for coordinates in input_values:
            coordinates = tuple([int(i) for i in coordinates])
            results.append(coordinates)
        return enumerate(results)


def calculate_distance(point1, point2):
    coordinates1 = point1
    coordinates2 = point2
    point1_x, point1_y, point1z = coordinates1
    point2_x, point2_y, point2z = coordinates2
    distance = sqrt((point1_x - point2_x) ** 2
                    + (point1_y - point2_y) ** 2
                    + (point1z - point2z) ** 2)
    x_sqrd = point1_x * point2_x
    return distance, x_sqrd


def calculate_shortest_distances(coordinates):
    coord_len = len(coordinates)
    distances = []
    junction_points = []
    for point in range(coord_len):
        junction_points.append(str(point))
        for next_p in range(point, coord_len):
            dist_a_b, x_sqrd = calculate_distance(coordinates[point], coordinates[next_p])
            if dist_a_b == 0:
                continue
            distances.append((str(point), str(next_p), dist_a_b, x_sqrd))
    distances.sort(key=lambda x: x[2])
    # print(f'length of coord = {coord_len}, distances: {distances}')
    print(coord_len)
    results = [[distances[0][0], distances[0][1]]]
    x_sqrd = distances[0][3]
    distances = distances[1:]

    # print(f'results: {results},'
    #       f'distances: {distances}')

    def check_for_merge(p_out, result_set):
        for circ in result_set:
            if p_out in circ:
                return circ

    def check_last_point_added(result_current):

        total_added = 0
        for circ in result_current:
            total_added += len(circ)
        # print(f'total_added: {total_added}')
        # print(len(result_current))
        if total_added == coord_len and len(result_current) == 1:
            return False
        else:
            return True

    distances_added = 2
    # print(f'distances_added : {distances_added}')
    last_point_added = True
    print(len(distances))
    while len(distances) > 0 and last_point_added:
        next_point = distances[0]
        results.sort(key=lambda x: len(x), reverse=True)
        p1 = next_point[0]
        p2 = next_point[1]
        x_sqrd = next_point[3]
        distances.pop(0)
        # print(
        #     f'distance_added: {distances_added}, '
        #     f'results: {results}, '
        #     f'next point {next_point},'
        #     f'length of results: {len(results)},'
        #     f'x_sqrd = {x_sqrd}'
        # )

        # dist_add_check = distances_added
        for circuit in results:
            # print(f'distance added: {distances_added}, ')
            if p1 in circuit and p2 in circuit:
                # distances.pop(0)
                # distances_added += 1
                break
            elif p1 in circuit and p2 not in circuit:
                # circuit.append(p2)
                # distances.pop(0)
                circ2 = check_for_merge(p2, results)
                # print(type(circ2))
                if circ2 is not None:
                    merged = circuit + circ2
                    results.remove(circuit)
                    results.remove(circ2)
                    results.append(merged)
                else:
                    circuit.append(p2)
                distances_added += 1
                break

            elif p2 in circuit and p1 not in circuit:

                circ2 = check_for_merge(p1, results)
                if circ2 is not None:
                    merged = circuit + circ2
                    results.remove(circuit)
                    results.remove(circ2)
                    results.append(merged)
                else:
                    circuit.append(p1)
                distances_added += 1
                break
            else:
                # print(f'p1: {p1}, p2: {p2}, circuit: {circuit}')
                if circuit == results[-1]:
                    results.append([p1, p2])
                    # distances.pop(0)
                    distances_added += 1
        last_point_added = check_last_point_added(results)

    # print(f'distances_added_end : {distances_added}')
    results.sort(key=lambda x: len(x), reverse=True)
    # print(f'results: {results}, length of results: {len(results)}, x_sqrd: {x_sqrd}')
    return results, x_sqrd


def main():
    input_values = get_input('./input2.txt')
    listed_coords = [coords for coords in input_values]
    # print(listed_coords)
    coords_dict = {junc: coord for junc, coord in listed_coords}
    # print(coords_dict)
    closest_junc = calculate_shortest_distances(coords_dict)
    print(closest_junc[1])


if __name__ == '__main__':
    main()
