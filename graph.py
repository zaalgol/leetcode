from collections import deque
class Node:
    def __init__(self, val = 0, neighbors = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
from queue import Queue
from typing import Optional

from enum import Enum


class State(Enum):
  kInit = 0
  kVisiting = 1
  kVisited = 2


class Solution:
    
                
    def numIslands(self, grid: list[list[str]]) -> int:
        
        count = 0
        lenj = len(grid[0])
        leng =len(grid)
        visited = [[False for _ in range(lenj)] for _ in range(leng)]
        for i in range(leng):
            for j in range(lenj):
                if not visited[i][j] and grid[i][j] == "1":
                    count +=1
                    q = Queue()
                    q.put((i,j))
                    while not q.empty():
                        y,x = q.get()
                        if y >=0 and x >=0 and y<leng and x < lenj and grid[y][x]  == "1" and not visited[y][x]:
                            visited[y][x] = True
                            q.put((y +1, x))
                            q.put((y, x +1))
                            q.put((y -1, x))
                            q.put((y, x -1))
        return count
                
                
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        leny=len(board)
        lenx=len(board[0])
        pathes =  ((0, 1), (1, 0), (0, -1), (-1, 0))

        def solve_helper(lenyy, lenxx, y_start=0, x_start=0):
            for y in range(y_start, lenyy):
                for x in range(x_start, lenxx):
                    if board[y][x] == "O":
                        q = Queue()
                        q.put((y,x))
                        while not q.empty():
                            y1, x1 = q.get()
                            if x1 >= 0 and x1 <  lenx and y1 >= 0 and y1 < leny and board[y1][x1] == "O":
                                board[y1][x1] = "OO"
                                for yd, xd in pathes:
                                    q.put((y1 +yd, x1+xd))

        solve_helper(leny, 1)
        solve_helper(leny, lenx, x_start=lenx-1)
        solve_helper(1, lenx)
        solve_helper( leny, lenx, y_start=leny-1)
        for y in range(leny):
            for x in range(lenx):
                if board[y][x] == "OO":
                    board[y][x] = "O"
                elif board[y][x] == "O":
                    board[y][x] = "X"
        
        
    
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:

        def bfs(source, target):
            visits = set()
            q = Queue()
            q.put([source, 1])
            while not q.empty():
                item, weight = q.get()
                if item not in visits:
                    if item == target:
                        return  weight
                    for n, w in d[item]:
                        q.put([n,weight *w] )
                    
                    visits.add(item)
            return -1


        output = []
        d = {} # x/y, value
        for i, v in enumerate(equations):
            if v[0] not in d:
                d[v[0]]=[]
            d[v[0]].append([v[1], values[i]])
            if v[1] not in d:
                d[v[1]]=[]
            d[v[1]].append([v[0], 1 / values[i]])
        
        for query in queries:
            if query[0] not in d or query[1] not in d:
                output.append(-1)
            else:
                output.append(bfs(query[0], query[1]))

        return output
    
    def clone_not_connectivity_graph(self, nodes):
        new_nodes = {}
        def dfs(node):
            if node in new_nodes:
                return new_nodes[node]
            
            clone  = Node(node.value)
            new_nodes[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone     


        for node in nodes:
            dfs(node)
        return new_nodes.values()

    def bfs(self, node):
        visited = set()
        q = deque()
        q.append(node)
        while q:
            node = q.popleft()
            if node not in visited:
                visited.add(node)
                print(node.val)
                for n in node.neighbors:
                    q.append(n)


    def dfs_and_print_tree_preorder(self, node):
        visited = set()
        stack = [node]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(node.val)
                for n in node.neighbors[::-1]:
                    stack.append(n)
    




    # def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
    #     graph = [[] for _ in range(numCourses)]
    #     states = [State.kInit] * numCourses

    #     for v, u in prerequisites:
    #         graph[u].append(v)

    #     def hasCycle(u: int) -> bool:
    #         if states[u] == State.kVisiting:
    #             return True
    #         if states[u] == State.kVisited:
    #             return False

    #         states[u] = State.kVisiting
    #         if any(hasCycle(v) for v in graph[u]):
    #             return True
    #         states[u] = State.kVisited

    #         return False

    #     return not any(hasCycle(i) for i in range(numCourses))

    # def hasCycle(self, states, u) -> bool:
    #     if states[u] == State.kVisiting:
    #         return True
    #     if states[u] == State.kVisited:
    #         return False

    #     states[u] = State.kVisiting
    #     if any(self.hasCycle(v) for v in graph[u]):
    #         return True
    #     states[u] = State.kVisited

    #     return False
                
solution = Solution()

# solution.canFinish(2, [[1,0],[0,1]])


solution.calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])


node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node3.neighbors.append(node1)
node3.neighbors.append(node5)

node3.neighbors.append(node1)
node3.neighbors.append(node5)

node1.neighbors.append(node0)
node1.neighbors.append(node2)

node5.neighbors.append(node4)
node5.neighbors.append(node6)
solution.dfs_and_print_tree_preorder(node3) # print tree

node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors.append(node2)
node1.neighbors.append(node0)

node2.neighbors.append(node0)
node2.neighbors.append(node3)
node2.neighbors.append(node4)

# node3.neighbors.append(node2)
# node3.neighbors.append(node4)

# node2.neighbors.append(node1)
# node2.neighbors.append(node3)
solution.bfs(node1)




r = solution.clone_not_connectivity_graph(node1)

solution.solve([["X","O","O","X","X","X","O","X","O","O"],["X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","O","X","X","X","X","X"],["X","O","X","X","X","O","X","X","X","O"],["O","X","X","X","O","X","O","X","O","X"],["X","X","O","X","X","O","O","X","X","X"],["O","X","X","O","O","X","O","X","X","O"],["O","X","X","X","X","X","O","X","X","X"],["X","O","O","X","X","O","X","X","O","O"],["X","X","X","O","O","X","O","X","X","O"]])
solution.solve([["O","O","O"],["O","O","O"],["O","O","O"]])
solution.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])


solution.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])


