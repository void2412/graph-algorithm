#Uses python3
import math
import sys
import queue



def Bellman_Ford(adj, cost, root):
    #get number of vertex
    size=len(adj)

    #init computing data
    dist = []
    prev =[]
    queueLast = queue.Queue()
    for i in range(size):
        dist.append(math.inf)
        prev.append(-1)

    #init value of root
    dist[root]=0
    
    #bellmanFord iteration
    for i in range(size):
        #get list of adj of vertex i
        adjList = adj[i]
        x = 0
        for vertex in adjList:
            if dist[vertex] > (dist[i] + cost[i][x]):
                dist[vertex] = dist[i] + cost[i][x]
                prev[vertex] = i
            if i == (size-1):
                queueLast.put(vertex)
            x += 1

    while queueLast.qsize() > 0:
        node = queueLast.get()
        beginNode = node
        for i in range(size):
            
            node = prev[node]
            if node == beginNode:
                return 1
    return 0


def negative_cycle(adj, cost):
    result = Bellman_Ford(adj, cost, 0)

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
