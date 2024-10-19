def topologicalSortUtil(v, adj, visited, stack):
    # Mark the current node as visited
    visited[v] = True

    # Recur for all adjacent vertices
    for i in adj[v]:
        if not visited[i]:
            topologicalSortUtil(i, adj, visited, stack)

    # Push current vertex to stack which stores the result
    stack.append(v)


# Function to perform Topological Sort
def topologicalSort(adj, V):
    # Stack to store the result
    stack = []

    visited = [False] * V

    # Call the recursive helper function to store
    # Topological Sort starting from all vertices one by
    # one
    for i in range(V):
        if not visited[i]:
            topologicalSortUtil(i, adj, visited, stack)

    # Print contents of stack
    print("Topological sorting of the graph:", end=" ")
    for v in stack[::-1]:
        print(v, end=" ")

def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    # Helper function to perform DFS and detect cycles
    def topologicalSortUtil(v, adj, visited, recursion_stack, stack):
        visited[v] = True
        recursion_stack[v] = True

        # Recur for all adjacent vertices
        for i in adj[v]:
            if not visited[i]:
                if not topologicalSortUtil(i, adj, visited, recursion_stack, stack):
                    return False
            elif recursion_stack[i]:
                # Found a cycle, return False
                return False

        recursion_stack[v] = False
        stack.append(v)
        return True

    # Build the adjacency list
    adj = [[] for _ in range(numCourses)]
    for prereq in prerequisites:
        adj[prereq[1]].append(prereq[0])  # reverse the order for topological sorting

    stack = []
    visited = [False] * numCourses
    recursion_stack = [False] * numCourses

    # Perform DFS from each node
    for i in range(numCourses):
        if not visited[i]:
            if not topologicalSortUtil(i, adj, visited, recursion_stack, stack):
                return []  # Cycle detected, return empty list
    print(stack)
    return stack  # Return the reverse of the topological sort order



# Driver code
if __name__ == "__main__":
    # V = 2
    # findOrder(2,[[0, 1], [1, 0]])
    V = 4
    findOrder(4,[[1,0],[2,0],[3,1],[3,2]])

    # Number of nodes
    V = 4

    # Edges
    edges = [[0, 1], [1, 2], [3, 1], [3, 2]]

    # Graph represented as an adjacency list
    adj = [[] for _ in range(V)]

    for i in edges:
        adj[i[0]].append(i[1])

    topologicalSort(adj, V)