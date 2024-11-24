from collections import defaultdict
import heapq


def dijkstra(g, src, target):
    q = [(0, src, [])]
    visited, dist = set(), {src: 0.0}
    while q:
        cost, v, path = heapq.heappop(q)
        if v not in visited:
            visited.add(v)
            path.append(v)
            if v == target:
                return (cost, path)
            
            for cost2, v2 in g.get(v, ()):
                if v2 in visited:
                    continue
                if cost + cost2 < dist.get(v2, float('inf')):
                    dist[v2] = cost + cost2
                    heapq.heappush(q, (cost + cost2, v2, path)) 
    return (float('inf'), ())

def if_one_difference(gen1, gen2):
    diff=0
    for i in range(8):
        if gen1[i] != gen2[i]:
            if diff > 0:
                return False
            diff +=1
    return True if diff==1 else False
    
def minMutation(startGene: str, endGene: str, bank: list[str]) -> int:
    if startGene == endGene:
        return 0
    

    def dijkstra(g, src, target):
        q = [(0, src, [])]
        visited, dist = set(), {src: 0.0}
        while q:
            cost, v, path = heapq.heappop(q)
            if v not in visited:
                visited.add(v)
                path.append(v)
                if v == target:
                    return cost
                
                for cost2, v2 in g.get(v, ()):
                    if v2 in visited:
                        continue
                    if cost + cost2 < dist.get(v2, float('inf')):
                        dist[v2] = cost + cost2
                        heapq.heappush(q, (cost + cost2, v2, path)) 
        return -1
    
    # build graph:
    graph=defaultdict(list)

    for i in range(len(bank)):
        if if_one_difference(bank[i], startGene):
            graph[startGene].append((1, bank[i]))
        for j in range(i + 1, len(bank)):
            if if_one_difference(bank[i], bank[j]):
                graph[bank[i]].append((1, bank[j]))
    found = False

    for i in range(len(bank)):
        if bank[i] == endGene:
            found = True
        if if_one_difference(bank[i], startGene):
            graph[startGene].append((1, bank[i]))
        for j in range(i + 1, len(bank)):
            if if_one_difference(bank[i], bank[j]):
                graph[bank[i]].append((1, bank[j]))
    if not found:
        return -1
    return dijkstra(graph, startGene, endGene)

if __name__ == '__main__':
    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    # bank = ["AACCGGTA"]
    # endGene = "AAACGGTA"
    # bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    bank =[]

    print(minMutation(startGene, endGene, bank))





    edges = [
        ('A', 'B', 7),
        ('A', 'D', 5),
        ('B', 'C', 8),
        ('B', 'D', 9),
        ('B', 'E', 7),
        ('C', 'E', 5),
        ('D', 'E', 15),
        ('D', 'F', 6),
        ('E', 'F', 8),
        ('E', 'G', 9),
        ('F', 'G', 11)
    ]
    g = defaultdict(list)
    for v, u, c in edges:
        g[v].append((c, u))
    src, target = 'A', 'G'
    print('{} -> {}:'.format(src, target))
    print(dijkstra(g, src, target))