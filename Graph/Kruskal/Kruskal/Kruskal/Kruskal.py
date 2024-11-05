# Disjoint set class to manage connected components
# SORT CAC VERTICE CO DUONG DI NGAN DAI
# USING DISJOIN CONNECT CAC DINH VOI NHAU
class DisjointSet:
    def __init__(self, vertices):
        # Initialize parent and rank dictionaries for each vertex
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        # Path compression heuristic
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        # Union by rank heuristic
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Kruskal's Algorithm to find Minimum Spanning Tree
def kruskal(graph):
    T = []  # Initialize MST as empty list

    # Extract vertices and initialize Disjoint Set for each vertex
    vertices = set([v for edge in graph for v in edge[:2]])
    ds = DisjointSet(vertices)

    # Sort edges in E by their weight
    graph.sort(key=lambda edge: edge[2])

    # Iterate over sorted edges
    for u, v, weight in graph:
        # Find the representatives of the sets containing u and v
        if ds.find(u) != ds.find(v):
            # If they belong to different sets, union them and add the edge to MST
            T.append((u, v, weight))
            ds.union(u, v)

    return T

# Example graph: list of edges (u, v, weight)
graph = [
    ('A', 'B', 2), ('A', 'C', 3), ('B', 'E', 4), ('B', 'G', 5),
    ('C', 'D', 1), ('D', 'E', 2), ('E', 'F', 4), ('F', 'G', 1)
]

# Running Kruskal's algorithm
T = kruskal(graph)

# Output the edges in the MST
print("Minimum Spanning Tree:", T)
