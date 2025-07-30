

'''
https://dmoj.ca/problem/ccc10s4

Labelling the area's as the nodes, and if 2 areas have an edge in common,
Then there will be an edge between them.

Now the question becomes:
If we choose a node u != 1,
what's the minimum cost from all 2 <= v <= n to reach u?
Or
what's the minimum cost from all 2 <= v <= n to reach 1?

In either case, this is just MST

Even though I was spoiled that this was MST, I don't think it's really hard
Once you realize what the true graph looks like, it's very obviously MST
'''

# W Data Structure
class UnionFind:

    def __init__(self, n):
        self.n = n
        self.p = [i for i in range(n + 1)]
        self.sz = [1] * (n + 1)

    def find_set(self, a):
        if self.p[a] == a:
            return a

        self.p[a] = self.find_set(self.p[a])
        return self.p[a]

    def same_set(self, a, b):
        return self.find_set(a) == self.find_set(b)

    def union(self, a, b):
        ra, rb = self.find_set(a), self.find_set(b)

        if self.sz[ra] < self.sz[rb]:
            ra, rb = rb, ra

        self.sz[ra] += self.sz[rb]
        self.p[rb] = ra

n = int(input())

# edge: [areas]
mp = {}

for _ in range(1, n + 1):
    info = list(map(int, input().split()))
    e = info[0]

    for i in range(1, e + 1):
        a, b = info[i], info[i + 1]
        if i == e:
            b = info[1]

        a, b = min(a, b), max(a, b)
        if (a, b) not in mp.keys():
            mp[(a, b)] = []
        mp[(a, b)].append([_, info[e + i]])

edges = []

# Find edges, 0 = outside
for i in mp.keys():
    if len(mp[i]) == 1:
        edges.append([0, mp[i][0][0], mp[i][0][1]])
    else:
        assert len(mp[i]) == 2
        edges.append([mp[i][0][0], mp[i][1][0], mp[i][1][1]])

edges.sort(key=lambda x: x[-1])

first = 0 # Go to node 0
second = 0 # Don't include 0

dsu1 = UnionFind(n)
dsu2 = UnionFind(n)

# Standard Kruskal
for u, v, w in edges:

    if not dsu1.same_set(u, v):
        dsu1.union(u, v)
        first += w

    if u != 0 and v != 0 and not dsu2.same_set(u, v):
        dsu2.union(u, v)
        second += w

print(min(first, second))
