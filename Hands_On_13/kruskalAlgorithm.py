class Edge:
    def __init__(self, weight, start, end):
        self.weight = weight
        self.start = start
        self.end = end

class UnionFind:
    def __init__(self, elements):
        self.parent = {elem: elem for elem in elements}
        self.rank = {elem: 0 for elem in elements}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1  
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2  
            else:
                self.parent[root2] = root1  
                self.rank[root1] += 1     

def kruskal(vertices, edges):
    edges.sort(key=lambda edge: edge.weight)
    
    uf = UnionFind(vertices)  
    mst = []  

    for edge in edges:
        if uf.find(edge.start) != uf.find(edge.end):
            uf.union(edge.start, edge.end)  
            mst.append(edge)  

    return mst

vertices = {"a", "b", "c", "d", "e", "f", "g", "h", "i"}
edges = [
    Edge(4, "a", "b"), Edge(8, "a", "h"), Edge(8, "b", "c"), Edge(11, "b", "h"),
    Edge(7, "c", "d"), Edge(4, "c", "f"), Edge(2, "c", "i"), Edge(6, "c", "g"),
    Edge(9, "d", "e"), Edge(14, "d", "f"), Edge(10, "e", "f"), Edge(2, "f", "g"),
    Edge(1, "g", "h"), Edge(7, "h", "i")
]

mst = kruskal(vertices, edges)
print("Minimum Spanning Tree (MST):")
for edge in mst:
    print(f"Edge {edge.start}-{edge.end} with weight {edge.weight}")
