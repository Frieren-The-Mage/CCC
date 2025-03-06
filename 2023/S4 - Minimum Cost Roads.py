import sys
from heapq import heappop, heappush
input = sys.stdin.readline

'''
https://dmoj.ca/problem/ccc23s4

Good graph problem with interesting solution
and though process.
We can consider each edge seperately and ask if we should
Include the edge or not include it.
The tricky part is well-defining edges that belong and don't belong to the plan.
Let's say we are considering on adding edge i, which connects nodes u, v.
We can check the distance from u to v if we add edge i, and if we don't.
'''
n, m = map(int, input().split())

adj_list = [[] for _ in range(n + 1)]
edges = []

for i in range(m):
    u, v, l, c = map(int, input().split())

    edges.append((u, v, l, c))

# Similar to Kruskal, sort edges by removing the best edges first
edges.sort(key=lambda x: x[3], reverse=True)

for i in range(m):
    u, v, l, c = edges[i]

    adj_list[u].append((v, l, c, i))
    adj_list[v].append((u, l, c, i))

dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]

# precalculate best distance
def dijkstra(start):

    dist[start][start] = 0
    heap = [(0, start)]
    # Running distance, current node

    while heap:
        d, node = heappop(heap)

        if d > dist[start][node]:
            continue

        for v, l, c, i in adj_list[node]:
            if d + l < dist[start][v]:
                dist[start][v] = d + l
                heappush(heap, (d + l, v))

removed = set()
def find_shortest(start, end):

    cur_dist = [float('inf')] * (n + 1) # to start node
    cur_dist[start] = 0

    heap = [(0, start)]
    # Running distance, current node

    while heap:
        d, node = heappop(heap)

        if node == end:
            return d

        if d > cur_dist[node]:
            continue

        for v, l, c, i in adj_list[node]:

            if i in removed:
                continue

            if d + l < cur_dist[v]:
                cur_dist[v] = d + l
                heappush(heap, (d + l, v))

    return float('inf')

for i in range(1, n + 1):
    dijkstra(i)

for i in range(m):
    u, v, l, c = edges[i]
    # For each edge, check if we can remove it
    removed.add(i)
    if find_shortest(u, v) > dist[u][v]:
        # Must keep the edge
        removed.remove(i)

ans = 0

for i in range(m):
    if i not in removed:
        ans += edges[i][3]

print(ans)
