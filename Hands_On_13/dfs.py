def dfs(vertex, adjacency_matrix, visited, labels):
    print(labels[vertex], end=" ")
    visited[vertex] = True

    for neighbor in range(len(adjacency_matrix)):
        if not visited[neighbor] and adjacency_matrix[vertex][neighbor] == 1:
            dfs(neighbor, adjacency_matrix, visited, labels)

def main():
    NUM_VERTICES = 7

    adjacency_matrix = [
        [0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
    ]

    visited = [False] * NUM_VERTICES
    labels = ["A", "B", "C", "D", "E", "F", "G"]

    print("DFS traversal:", end=" ")

    for vertex in range(NUM_VERTICES):
        if not visited[vertex]:
            dfs(vertex, adjacency_matrix, visited, labels)

if __name__ == "__main__":
    main()
