def calculate_paths(matrix):
    size = len(matrix)
    costs = [[matrix[row][col] for col in range(size)] for row in range(size)]
    successors = [[None if matrix[row][col] == float('inf') else col for col in range(size)] for row in range(size)]

    for intermediate in range(size):
        for start in range(size):
            for end in range(size):
                if costs[start][intermediate] + costs[intermediate][end] < costs[start][end]:
                    costs[start][end] = costs[start][intermediate] + costs[intermediate][end]
                    successors[start][end] = successors[start][intermediate]

    return costs, successors

def build_path(successors, start, end):
    if successors[start][end] is None:
        return None
    path = [start]
    while start != end:
        start = successors[start][end]
        path.append(start)
    return path

graph1 = [
    [0, 2, float('inf'), 1, float('inf')],
    [float('inf'), 0, 3, float('inf'), float('inf')],
    [float('inf'), float('inf'), 0, 4, 5],
    [float('inf'), float('inf'), 1, 0, float('inf')],
    [3, float('inf'), float('inf'), float('inf'), 0]
]

graph2 = [
    [0, 7, float('inf'), 2],
    [float('inf'), 0, 5, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [6, float('inf'), 4, 0]
]

distances1, successors1 = calculate_paths(graph1)
distances2, successors2 = calculate_paths(graph2)

paths1 = {}
for source in range(len(graph1)):
    for destination in range(len(graph1)):
        paths1[(source, destination)] = build_path(successors1, source, destination)

paths2 = {}
for source in range(len(graph2)):
    for destination in range(len(graph2)):
        paths2[(source, destination)] = build_path(successors2, source, destination)

print("Graph 1 - Distance Matrix:")
for row in distances1:
    print(row)

print("\nGraph 1 - Paths:")
for (start, end), path in paths1.items():
    print(f"From {start} to {end}: {path}")

print("\nGraph 2 - Distance Matrix:")
for row in distances2:
    print(row)

print("\nGraph 2 - Paths:")
for (start, end), path in paths2.items():
    print(f"From {start} to {end}: {path}")
