
# import heapq

# # Function to implement Dijkstra's Algorithm
# def dijkstra(graph, start):
#     # Initialize the shortest distance dictionary with infinity for all vertices
#     shortest_distances = {vertex: float('infinity') for vertex in graph}
#     # Set the distance for the start node to 0
#     shortest_distances[start] = 0

#     # Priority queue to store the vertices to explore (min-heap)
#     priority_queue = [(0, start)]  # (distance, vertex)
    
#     # Previous nodes dictionary to store the path
#     previous_nodes = {vertex: None for vertex in graph}
    
#     while priority_queue:
#         # Get the vertex with the smallest distance
#         current_distance, current_vertex = heapq.heappop(priority_queue)

#         # Skip this vertex if we've already found a shorter path
#         if current_distance > shortest_distances[current_vertex]:
#             continue

#         # Explore neighbors of the current vertex
#         for neighbor, weight in graph[current_vertex]:
#             distance = current_distance + weight

#             # Only consider this new path if it's shorter
#             if distance < shortest_distances[neighbor]:
#                 shortest_distances[neighbor] = distance
#                 previous_nodes[neighbor] = current_vertex
#                 heapq.heappush(priority_queue, (distance, neighbor))

#     return shortest_distances, previous_nodes

# # Function to reconstruct the shortest path from start to target
# def shortest_path(previous_nodes, start, target):
#     path = []
#     current_vertex = target

#     while current_vertex is not None:
#         path.append(current_vertex)
#         current_vertex = previous_nodes[current_vertex]

#     # Reverse the path to get the correct order from start to target
#     path = path[::-1]

#     if path[0] == start:
#         return path
#     else:
#         return None  # No path found

# # Example graph as an adjacency list
# graph = {
#     'A': [('B', 7), ('E', 3)],
#     'B': [('A', 7), ('E', 1), ('C', 6), ('D', 2)],
#     'C': [('B', 6), ('D', 4)],
#     'D': [('B', 2), ('C', 4), ('E', 2)],
#     'E': [('A', 3), ('B', 1), ('D', 2)],
# }

# # Running Dijkstra's algorithm from node 'A'
# distances, previous_nodes = dijkstra(graph, 'A')

# # Output shortest distances from A to all other vertices
# print("Shortest distances from A:", distances)

# # Output the shortest path from A to C
# path = shortest_path(previous_nodes, 'A', 'C')
# print("Shortest path from A to C:", path)



def dijkstra_no_heap(graph, start):
  
    shortest_distances = {vertex: float('infinity') for vertex in graph}
    
  
    shortest_distances[start] = 0

   
    previous_nodes = {vertex: None for vertex in graph}

   
    unvisited = set(graph.keys())

   
    known_status = {vertex: False for vertex in graph}

   
    while unvisited:
     
        current_vertex = min(
            (vertex for vertex in unvisited),
            key=lambda vertex: shortest_distances[vertex],
            default=None
        )

    
        if shortest_distances[current_vertex] == float('infinity'):
            break

      
        known_status[current_vertex] = True
        unvisited.remove(current_vertex)

       
        for neighbor, weight in graph[current_vertex]:
          
            distance = shortest_distances[current_vertex] + weight

            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex

  
    return shortest_distances, previous_nodes, known_status

  
def shortest_path(previous_nodes, start, target):
    path = []
    current_vertex = target

  
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_nodes[current_vertex]

  
    path = path[::-1]

   
    if path[0] == start:
        return path
    else:
        return None  
