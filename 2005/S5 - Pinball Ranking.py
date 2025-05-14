'''
https://dmoj.ca/problem/ccc05s5
Interesting problem, involving Coordinate Compression and Segment Tree
Notice that number of elements is small, each element is big
Map each element to it's index in the sorted structure, now use those elements
Segment Tree to query number of elements greater than it
'''

import sys
from math import ceil, log2

input = sys.stdin.readline

n = int(input())

original = [int(input()) for _ in range(n)]
vals = sorted(original)

unique = [vals[0]]

for i in range(1, n):
    if vals[i] != vals[i - 1]:
        unique.append(vals[i])

sz = 2 ** ceil(log2(n))

seg_tree = [0] * (2 * sz)
# Keep track of the frequencies

convert = lambda x: sz + x

def update(val):
    indx = convert(val)

    seg_tree[indx] += 1
    indx //= 2

    while indx:
        seg_tree[indx] += 1
        indx //= 2

def query(l, r):
    l, r = convert(l), convert(r)

    ans = 0
    cur = l
    rightmost_leaf = l
    jump = 1

    while cur <= r:
        if cur % 2 == 1 or rightmost_leaf + jump > r:
            ans += seg_tree[cur]
            cur = rightmost_leaf + 1
            rightmost_leaf = cur
            jump = 1

        else:
            cur //= 2
            rightmost_leaf += jump
            jump *= 2

    return ans

ans = 0

for i in original:
    l = 0
    r = len(unique) - 1

    # Find index in sorted structure, also its compressed value
    while l <= r:
        mid = (l + r) // 2

        if unique[mid] == i:
            l = mid
            break

        elif unique[mid] < i:
            l = mid + 1

        else:
            r = mid - 1

    update(l)

    ans += 1 + query(l + 1, len(unique) - 1)

print(ans / n)


