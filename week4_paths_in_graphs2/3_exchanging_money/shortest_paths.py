#Uses python3

import sys
import queue

def Bellman_Ford(adj, cost, root, dist):
    #get number of vertex
    size=len(adj)

    #init computing data
    prev =[]
    queueLast = queue.Queue()
    for i in range(size):
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
    
    return (queueLast, prev)



def findNegCycle(adj, cost, queueV, prev):
    while queueV.qsize() > 0:
        negativeCycle = []
        node = queueV.get()
        negativeCycle.append(node)

        for i in range(size):
            nodeP = prev[node]
            if nodeP == beginNode:
                return negativeCycle
            else:
                negativeCycle.append(nodeP)
    pass

def shortet_paths(adj, cost, s, distance, reachable, shortest):
    
    pass


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

