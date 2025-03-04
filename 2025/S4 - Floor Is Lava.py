import sys
from heapq import heappop, heappush
input = sys.stdin.readline

'''
https://dmoj.ca/problem/ccc25s4
Interesting graph problem
First observe that unlike normal Dijkstra's
you cannot find the shortest path to a node
by looking at the previous shortest path's
to its neighbors.

So to find the shortest path to a node:
1. Look at all it's neighbors
2. Find all possible edges you possibly could've gotten to that neighbor
3. Find the shortest path ending at the edge in step 2, and compare

This can be done with a Dijkstra based on the edges, instead of the nodes
I labeled the edges 1, 2, ... M
And to make things easier, I added 1 new edge and 1 new node
0 1 0 (An edge from node 0 to node 1 with weight 0)
'''

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, m = map(int, input().split())

adj_list = [[] for _ in range(n + 1)]
adj_list[1].append((0, 0, 0))

edges = [0]
# Define edges[i] = weight of the ith edge

for i in range(1, m + 1):
    a, b, c = map(int, input().split())

    adj_list[a].append((b, c, i))
    adj_list[b].append((a, c, i))

    edges.append(c)

dist = [1 << 60] * (m + 1)
# Define dist[i] = min cost found so far such that
# i is the last road

# Base Case
dist[0] = 0

heap = [(0, 1, 0)]
# Running cost, current node, previous edge index

while heap:
    cost, node, prev = heappop(heap)
    val = edges[prev]

    if cost > dist[prev]:
        # Not most optimal path
        continue
    
    if node == n:
        # Found answer, no need to Dijkstra any further
        print(cost)
        break

    for v, c, i in adj_list[node]:
        if cost + abs(val - c) < dist[i]:
            dist[i] = cost + abs(val - c)

            heappush(heap, (cost + abs(val - c), v, i))
