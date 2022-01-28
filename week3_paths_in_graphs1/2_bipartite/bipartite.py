#Uses python3

import sys
import queue

def bipartite(adj):
    #write your code here
    res = checkBipartite(adj, 0)
    return res


def checkBipartite(adj, s):
    #write your code here
    color = []
    
    for i in range(len(adj)):
        color.append(-1)
    
    color[s] = 0
    q = queue.Queue()
    q.put(s)
    while q.qsize() > 0:
        node = q.get()
        for vertex in adj[node]:
            if color[vertex] == -1:
                q.put(vertex)
                
                #set color for vertex base on node
                if color[node] == 1:
                    color[vertex] = 0
                if color[node] == 0:
                    color[vertex] = 1
            elif color[vertex] == color[node]:
                return 0
    return 1
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
