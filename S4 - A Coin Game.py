
# https://dmoj.ca/problem/ccc12s4
# Kinda cool problem, just BFS but I missed the bitmask idea
# The bitmask idea is definitely cool, but boring problem otherwise

import sys
from collections import deque

input = sys.stdin.readline

def solve(n):
    arr = list(map(int, input().split()))
    for i in range(n):
        arr[i] -= 1

    def get_top(mask):
        for i in range(n):
            if mask & (1 << i):
                return i

    def next_states(cur):
        ans = []

        for i in range(n):
            if cur[i] == 0:
                continue

            for d in range(-1, 2, 2):
                j = i + d

                if not (0 <= j < n):
                    continue

                a = get_top(cur[i])

                if cur[j] == 0 or a < get_top(cur[j]):
                    next = cur.copy()
                    next[i] ^= (1 << a)
                    next[j] ^= (1 << a)
                    ans.append(next)
                    continue

        return ans

    visited = set()
    change = lambda x: tuple(i for i in x)

    start = [1 << i for i in arr]
    goal = [1 << i for i in range(n)]

    queue = deque([(start, 0)])

    while queue:
        state, dist = queue.popleft()

        if state == goal:
            print(dist)
            return

        for next in next_states(state):
            if change(next) not in visited:
                visited.add(change(next))
                queue.append((next, dist + 1))

    print('IMPOSSIBLE')

while True:
    n = int(input())

    if n == 0:
        break
    solve(n)
