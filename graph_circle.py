
from enum import Enum


class State(Enum):
  kNotVisited = 0
  kVisiting = 1
  kVisited = 2

def is_cyc_directed_util(adj, u, visited):
    if visited[u]==State.kVisiting:
        return True
    
    if visited[u]==State.kNotVisited:
        visited[u]=State.kVisiting
        for x in adj[u]:
            if is_cyc_directed_util(adj, x, visited):
                return True

    # Remove the vertex from recursion stack
    visited[u]= State.kVisited
    return False

def is_cyclic_directed(adj, V):
    visited = [State.kNotVisited] * V

    # Call the recursive helper function to
    # detect cycle in different DFS trees
    for i in range(V):
        if visited[i]==State.kNotVisited and is_cyc_directed_util(adj, i, visited):
            return True

    return False

def is_cyc_not_directed_util(adj, u, father, visited):
    if visited[u]==True:
        return True
    visited[u]=True
    

    for x in adj[u]:
        if father != None and x==father:
            continue
        if is_cyc_not_directed_util(adj, x, u, visited):
            return True

    # Remove the vertex from recursion stack
    return False

def is_cyclic_not_directed(adj, V):
    visited = [False] * V
    # Call the recursive helper function to
    # detect cycle in different DFS trees
    for i in range(V):
        if not visited[i] and is_cyc_not_directed_util(adj, i, None, visited):
            return True

    return False

# Driver function
if __name__ == "__main__":
    V = 10
    adj = [[] for _ in range(V)]

    # Adding edges to the graph
    adj[0].append(1)
    adj[1].append(0)
    adj[0].append(2)
    adj[2].append(0)
    # adj[2].append(0)
    # adj[2].append(3)
    if is_cyclic_not_directed(adj, V):
        print("not_directed Contains Cycle")
    else:
        print("not_directed No Cycle")


        V = 10
    adj = [[] for _ in range(V)]

    # Adding edges to the graph
    adj[0].append(1)
    adj[1].append(0)
    adj[0].append(2)
    adj[2].append(0)
    adj[2].append(1)
    adj[1].append(2)
    if is_cyclic_not_directed(adj, V):
        print("not_directed Contains Cycle")
    else:
        print("not_directed No Cycle")




    adj = [[] for _ in range(V)]

    # Adding edges to the graph
    adj[0].append(1)
    adj[0].append(2)
    adj[1].append(2)
    adj[2].append(0)
    adj[2].append(3)
    # adj[3].append(3)

    # Function call
    if is_cyclic_directed(adj, V):
        print("Contains Cycle")
    else:
        print("No Cycle")

    adj = [[] for _ in range(V)]

    # Adding edges to the graph
    adj[0].append(1)
    adj[0].append(2)
    adj[1].append(2)
    # adj[2].append(0)
    adj[2].append(3)
    # adj[3].append(3)

    # Function call
    if is_cyclic_directed(adj, V):
        print("Contains Cycle")
    else:
        print("No Cycle")

    adj = [[] for _ in range(V)]
    adj[0].append(1)
    adj[0].append(2)
    adj[1].append(2)
    adj[2].append(0)
    adj[2].append(3)
    adj[3].append(2)
    # adj[3].append(3)

    # Function call
    if is_cyclic_directed(adj, V):
        print("Contains Cycle")
    else:
        print("No Cycle")


    adj = [[] for _ in range(V)]
    adj[0].append(1)
    adj[0].append(2)
    adj[1].append(2)
    # adj[0].append(3)
    # adj[2].append(3)
    # adj[3].append(2)
    # adj[3].append(3)

    # Function call
    if is_cyclic_directed(adj, V):
        print("Contains Cycle")
    else:
        print("No Cycle")


    adj = [[] for _ in range(V)]
    adj[0].append(1)
    adj[0].append(2)
    adj[1].append(2)
    adj[0].append(3)
    adj[2].append(3)
    adj[3].append(4)
    adj[4].append(5)
    adj[2].append(5)
    adj[5].append(3)

    # Function call
    if is_cyclic_directed(adj, V):
        print("Contains Cycle")
    else:
        print("No Cycle")


    