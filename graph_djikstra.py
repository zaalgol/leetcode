import heapq

def dijkstra(graph, start):
    # Initialize the shortest paths dictionary with infinite distances
    shortest_paths = {vertex: float('inf') for vertex in graph}
    shortest_paths[start] = 0

    # Priority queue to keep track of the minimum distance to each vertex
    priority_queue = [(0, start)]  # (distance, vertex)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If the distance in the queue is greater than the already found shortest distance, skip it
        if current_distance > shortest_paths[current_vertex]:
            continue

        # Explore neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # If the new distance to the neighbor is shorter, update the shortest path
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1},
}

start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

print(f"Shortest paths from {start_vertex}: {shortest_paths}")


def dijkstra_path(graph, start):
    # Initialize the shortest paths dictionary and the predecessors dictionary
    shortest_paths = {vertex: float('inf') for vertex in graph}
    shortest_paths[start] = 0
    predecessors = {vertex: None for vertex in graph}
    
    # Priority queue to keep track of the minimum distance to each vertex
    priority_queue = [(0, start)]  # (distance, vertex)
    i = 0
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        print(i)
        print(current_vertex)
        i +=1
        
        # If the distance in the queue is greater than the already found shortest distance, skip it
        if current_distance > shortest_paths[current_vertex]:
            continue

        # Explore neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            print(i)
            i +=1
            # If the new distance to the neighbor is shorter, update the shortest path
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths, predecessors

def reconstruct_path(predecessors, start, end):
    path = []
    current_vertex = end
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = predecessors[current_vertex]
    path.reverse()
    return path if path[0] == start else []

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1},
}

start_vertex = 'A'
shortest_paths, predecessors = dijkstra_path(graph, start_vertex)

print(f"Shortest paths from {start_vertex}: {shortest_paths}")
print("Paths:")

for vertex in graph:
    if vertex != start_vertex:
        path = reconstruct_path(predecessors, start_vertex, vertex)
        if path:
            print(f"Path to {vertex}: {' -> '.join(path)}")
        else:
            print(f"No path to {vertex} found.")