import heapq

def shortest_path(graph, start):
    pq = []
    heapq.heappush(pq, (0, start))
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (new_dist, neighbor))

    return distances, predecessors

graph = {
    's': [('t', 3), ('y', 5)],
    't': [('y', 2), ('x', 6)],
    'y': [('t', 1), ('x', 4), ('z', 6)],
    'x': [('z', 2)],
    'z': [('s', 3), ('x', 7)]
}

distances, predecessors = shortest_path(graph, 's')

print("Shortest distances from 's':")
for node, dist in distances.items():
    print(f"{node}: {dist}")

print("\nPaths from 's':")
for node in predecessors:
    path = []
    current = node
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]
    print(f"{node}: {' -> '.join(path)}")
