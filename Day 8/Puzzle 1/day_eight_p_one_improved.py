from math import sqrt


def get_input(filename):
    """Read and parse junction box coordinates."""
    with open(filename, 'r') as file:
        coordinates = []
        for line in file:
            coords = tuple(map(int, line.strip().split(',')))
            coordinates.append(coords)
        return coordinates


def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two 3D points."""
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


def main():
    # Read input
    coordinates = get_input('./input2.txt')
    n = len(coordinates)
    
    # Calculate all pairwise distances
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = calculate_distance(coordinates[i], coordinates[j])
            distances.append((dist, i, j))
    
    # Sort by distance
    distances.sort(key=lambda x: x[0])
    
    print(len(distances))  # Total number of pairs
    
    # Initialize circuits list (replicating original algorithm behavior)
    # Start with the shortest distance
    circuits = [[str(distances[0][1]), str(distances[0][2])]]
    connections_made = 1
    distances = distances[1:]  # Remove the first distance
    
    def check_for_merge(p_out, result_set):
        """Check if a point is in any circuit and return that circuit."""
        for circ in result_set:
            if p_out in circ:
                return circ
        return None
    
    # Process distances until we make 1000 connections
    while len(distances) > 0 and connections_made < 1000:
        dist, i, j = distances[0]
        p1, p2 = str(i), str(j)
        distances = distances[1:]
        
        # Check each circuit
        for circuit in circuits:
            if p1 in circuit and p2 in circuit:
                # Both already in same circuit - skip
                break
            elif p1 in circuit and p2 not in circuit:
                # p1 in circuit, p2 not - check if p2 is in another circuit
                circ2 = check_for_merge(p2, circuits)
                if circ2 is not None:
                    # Merge the two circuits
                    merged = circuit + circ2
                    circuits.remove(circuit)
                    circuits.remove(circ2)
                    circuits.append(merged)
                else:
                    # p2 not in any circuit, add it
                    circuit.append(p2)
                connections_made += 1
                break
            elif p2 in circuit and p1 not in circuit:
                # p2 in circuit, p1 not - check if p1 is in another circuit
                circ2 = check_for_merge(p1, circuits)
                if circ2 is not None:
                    # Merge the two circuits
                    merged = circuit + circ2
                    circuits.remove(circuit)
                    circuits.remove(circ2)
                    circuits.append(merged)
                else:
                    # p1 not in any circuit, add it
                    circuit.append(p1)
                connections_made += 1
                break
            else:
                # Neither point in this circuit - check if we're at the last circuit
                if circuit == circuits[-1]:
                    circuits.append([p1, p2])
                    connections_made += 1
    
    print(len(circuits))  # Number of circuits
    
    # Sort circuits by size (descending)
    circuits.sort(key=len, reverse=True)
    print(circuits)
    
    # Multiply the sizes of the three largest circuits
    if len(circuits) >= 3:
        result = len(circuits[0]) * len(circuits[1]) * len(circuits[2])
    else:
        result = 0
    
    print(result)


if __name__ == '__main__':
    main()

