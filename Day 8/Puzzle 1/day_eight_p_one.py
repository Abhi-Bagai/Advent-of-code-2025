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
    return distance


def calculate_shortest_distances(coordinates):
    distances = []
    for point in range(len(coordinates)):
        for next_p in range(point, len(coordinates)):
            dist_a_b = calculate_distance(coordinates[point], coordinates[next_p])
            if dist_a_b == 0:
                continue
            distances.append((str(point), str(next_p), dist_a_b))
    distances.sort(key=lambda x: x[2])
    print(len(distances))
    shortest_distances = [distances[0][0], distances[0][1]]
    distances = distances[1:1000]

    results = [shortest_distances]

    print(f'results: {results}')

    def check_for_merge(p_out, result_set):
        for circ in result_set:
            if p_out in circ:
                return circ

    distances_added = 2
    print(f'distances_added : {distances_added}')
    while len(distances) > 0:
        next_point = distances[0]
        results.sort(key=lambda x: len(x), reverse=True)
        total = None
        if len(results) >= 3:
            total = get_total(results[:3])
        # print(
        #     f'distance_added: {distances_added}, '
        #     f'results: {results}, '
        #     f'next point {next_point},'
        #     f'length of results: {len(results)},'
        #     f'total: {total}')
        p1 = next_point[0]
        p2 = next_point[1]
        distances.pop(0)
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
    print(f'distances_added_end : {distances_added}')
    print(len(results))
    results.sort(key=lambda x: len(x), reverse=True)
    print(f'results: {results}, length of results: {len(results)}')
    return results


def get_total(circuits):
    total = 1
    for circuit in circuits:
        # print(f'length of circuit: {len(circuit)}')
        total *= len(circuit)
    return total


def main():
    input_values = get_input('./input2.txt')
    listed_coords = [coords for coords in input_values]
    # print(listed_coords)
    coords_dict = {junc: coord for junc, coord in listed_coords}
    # print(coords_dict)
    # print(calculate_distance(listed_coords[0][1], listed_coords[1][1]))
    # print(calculate_distance(coords_dict[0], coords_dict[1]))
    closest_junc = calculate_shortest_distances(coords_dict)
    # print(closest_junc)
    total = get_total(closest_junc[0:3])
    print(total)


if __name__ == '__main__':
    main()
