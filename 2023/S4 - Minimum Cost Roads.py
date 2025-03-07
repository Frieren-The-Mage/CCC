from heapq import heappop, heappush

'''
https://dmoj.ca/problem/ccc23s4

Good graph problem with interesting solution
and though process.
Motivation for problem is a bit hard.
We can do a Kruskal-like algorithm to check each edge, starting with the shortest,
and see if we should add it to our solution.
Unlike Kruskal where the deciding factor is if they are in the same set, the deciding factor is if the edge
yields a smaller distance than currently found.
'''

n, m = map(int, input().split())

edges = []
adj_list = [[] for _ in range(n + 1)]

for i in range(m):
    u, v, l, c = map(int, input().split())

    edges.append((u, v, l, c))

# Sort by distance first, then cost
edges.sort(key=lambda x: (x[2], x[3]))

# dijkstra to decide if we should add edge
def dijkstra(start, end):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0

    heap = [(0, start)]

    while heap:
        d, node = heappop(heap)

        if node == end:
            return d

        for v, l, c in adj_list[node]:
            if d + l < dist[v]:
                dist[v] = d + l
                heappush(heap, (d + l, v))

    return float('inf')

tot = 0
for i in range(m):
    u, v, l, c = edges[i]

    # New edge yields shorter value than currently found
    if dijkstra(u, v) > l:
        tot += c

        # We can access new edges now
        adj_list[u].append((v, l, c))
        adj_list[v].append((u, l, c))

print(tot)
