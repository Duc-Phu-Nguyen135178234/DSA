
import heapq

## co the bat dau tu bat dau root
## sau co expand , update parent 

def prim(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start, None)]  # (weight, vertex, parent)

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)
        if u not in visited:
            visited.add(u)
            if parent:
                mst.append((parent, u, weight))
            
            # Add neighbors to the heap
            for v, w in graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (w, v, u))

    return mst

# Example graph as adjacency list
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('E', 4), ('G', 5)],
    'C': [('A', 3), ('D', 1)],
    'D': [('C', 1), ('E', 2)],
    'E': [('B', 4), ('D', 2), ('F', 4)],
    'F': [('E', 4), ('G', 1)],
    'G': [('B', 5), ('F', 1)]
}

# Running Prim's algorithm starting from vertex 'A'
mst = prim(graph, 'A')

# Output the edges in the MST
print("Minimum Spanning Tree:", mst)

