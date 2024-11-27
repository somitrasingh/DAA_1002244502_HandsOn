class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

class Vertex:
    def __init__(self, value):
        self.value = value
        self.distance = float('inf')
        self.previous = None

def relax(source, target, weight):
    if target.distance > source.distance + weight:
        target.distance = source.distance + weight
        target.previous = source

def setup_graph(graph, start):
    for vertex in graph.vertices:
        vertex.distance = float('inf')
        vertex.previous = None
    start.distance = 0

def process_graph(graph, start):
    setup_graph(graph, start)
    for _ in range(len(graph.vertices) - 1):
        for (source, target) in graph.weights.keys():
            relax(source, target, graph.weights[(source, target)])
    for (source, target) in graph.weights.keys():
        if target.distance > source.distance + graph.weights[(source, target)]:
            return False
    return True

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = {}
        self.weights = {}
        for vertex in vertices:
            self.edges[vertex] = []

    def add_edge(self, start, end, weight):
        if start not in self.edges.keys():
            self.edges[start] = [end]
        else:
            self.edges[start].append(end)
        self.weights[(start, end)] = weight

    def __str__(self):
        print("\n ---Graph Connections---")
        for vertex in self.edges.keys():
            print(vertex.value, end=": ")
            for neighbor in self.edges[vertex]:
                print(neighbor.value, end=" ")
            print()
        return "---End of Connections---\n"

if __name__ == "__main__":
    vertices = [Vertex(i) for i in range(5)]
    edges = [Edge(vertices[0], vertices[1], 6),
             Edge(vertices[0], vertices[3], 7),
             Edge(vertices[1], vertices[2], 5),
             Edge(vertices[1], vertices[3], 8),
             Edge(vertices[1], vertices[4], -4),
             Edge(vertices[2], vertices[1], -2),
             Edge(vertices[3], vertices[2], -3),
             Edge(vertices[3], vertices[4], 9),
             Edge(vertices[4], vertices[0], 2),
             Edge(vertices[4], vertices[2], 7)]
    graph = Graph(vertices)
    for edge in edges:
        graph.add_edge(edge.start, edge.end, edge.weight)
    for key in graph.weights.keys():
        print(key, graph.weights[key])
    print(len(graph.weights.keys()))
    print(process_graph(graph, vertices[0]))
