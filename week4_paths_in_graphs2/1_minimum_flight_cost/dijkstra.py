#Uses python3

import sys
import math


class heapQueue():
    def __init__(self):
        self.queue = []
        self.size = -1
    
    def parent(self, i):
        return (i-1) // 2
    
    def leftChild(self, i):
        return ((2*i)+1)
    
    def rightChild(self, i):
        return ((2*i)+2)

    def shiftUp(self, i):
        while (i > 0 and self.queue[self.parent(i)][0] > self.queue[i][1]):
            self.swap(self.parent(i), i)
            i = self.parent(i)
    
    def shiftDown(self, i):
        minIndex = i

        left = self.leftChild(i)
        if (left <= self.size and self.queue[left][1] < self.queue[minIndex][1]):
            minIndex = left

        right = self.rightChild(i)
        if(right <= self.size and self.queue[right][1] < self.queue[minIndex][1]):
            minIndex = right

        if (i != minIndex):
            self.swap(i, minIndex)
            self.shiftDown(minIndex)
    
    def insert(self, item):
        self.size += 1
        self.queue.append(item)
        self.shiftUp(self.size)

    def extractMin(self):
        result = self.queue[0]
        self.queue[0] = self.queue[self.size]
        self.size -= 1
        self.shiftDown(0)

        return result
    
    def isEmpty(self):
        if self.size == -1:
            return True
        return False

    def swap(self, i , j):
        temp = self.queue[i]
        self.queue[i] = self.queue[j]
        self.queue[j] = temp
        pass

def distance(adj, cost, s, t):
    size = len(adj)
    dist = []
    prev = []
    processed = []
    for i in range(size):
        dist.append(math.inf)
        prev.append(-1)
        processed.append(False)
    q = heapQueue()
    dist[s] = 0
    for i in range(size):
        q.insert((i,dist[i]))
    
    while q.isEmpty() == False:
        (node,distVal) = q.extractMin()
        if processed[node] == False:
            i = 0
            for vertex in adj[node]:
                if dist[vertex] > (dist[node] + cost[node][i]):
                    dist[vertex] = dist[node] + cost[node][i]
                    prev[vertex] = node
                q.insert((vertex, dist[vertex]))
                i += 1
            processed[node] = True
    
    if dist[t] == math.inf:
        return -1
    
    return dist[t]
    


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
