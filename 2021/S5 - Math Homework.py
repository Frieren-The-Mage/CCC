
'''
https://dmoj.ca/problem/ccc21s5

Actually extremely easy once you read the problem
Lets say index i is covered by 2 ranges, Z1 and Z2
We know that Z1 | Ai, Z2 | Ai, so lcm(Z1, Z2) | Ai
So every element is just the lcm of all the ranges.

To calculate this, note that lcm is really just max, on the prime powers
We can do this by using a heap to find maximum while supporting adding and removing
Since Z <= 16, storing each prime power in a heap will pass

To find out of it's impossible, we simply use a sparse table to compute the gcd
'''

import sys
from math import gcd, floor, log2
from heapq import heappop, heappush

n, m = map(int, input().split())

heaps = [[] for _ in range(6)]
rem = [[] for _ in range(6)] # Rem is Best Girl

primes = [2, 3, 5, 7, 11, 13]

def update(h1, h2):
    while h1 and h2 and h1[0] == h2[0]:
        heappop(h1)
        heappop(h2)

diff = [[] for _ in range(n + 1)]

queries = []

for i in range(m):
    x, y, z = map(int, input().split())

    # 1-indexing to 0-indexing
    x -= 1
    y -= 1

    queries.append((x, y, z))

    diff[x].append(z)
    diff[y + 1].append(-1 * z)

arr = []

for i in range(n):
    for each in diff[i]:
        for j, p in enumerate(primes):
            val = 0
            while abs(each) % p == 0:
                val += 1
                each //= p

            if each < 0:
                heappush(rem[j], -1 * val)

            else:
                heappush(heaps[j], -1 * val)

    cur = 1
    for j in range(len(heaps)):
        update(heaps[j], rem[j])

    for j, p in enumerate(primes):
        if not heaps[j]:
            continue
        cur *= p ** (-1 * heaps[j][0])

    arr.append(cur)

# Sparse Table to find out if it's actually possible
sz = floor(log2(n))
sparse = [[0] * (sz + 1) for _ in range(n)]

for i in range(n):
    sparse[i][0] = arr[i]

for l in range(1, sz + 1):
    for i in range(n - (1 << l) + 1):
        sparse[i][l] = gcd(sparse[i][l - 1], sparse[i + (1 << (l - 1))][l - 1])

def query(l, r):
    s = floor(log2(r - l + 1))
    return gcd(sparse[l][s], sparse[r - (1 << s) + 1][s])

for x, y, z in queries:
    if query(x, y) != z:
        print('Impossible')
        sys.exit()

print(*arr)
