
# https://dmoj.ca/problem/ccc24s3

'''
Interesting Ad Hoc problem
Bruh coding moment, spent a week on this problem in the past and gave up,
but found idea in class in school in 40 minutes

First some important observations:

No swap can be fully contained by another swap
Formally, there cannot exist 2 swaps [l, r] and [l', r'] such that l < l' < r and l < r' < r

All left swaps are done in sorted order of their end point
All right swaps are done in reverse sorted order of their end point

Algorithm Steps:

Note: I considered [i, i] as a swap left, but it doesn't matter

Store indices of the values ofA A

First, keep track of the rightmost endpoint of all your left swaps so far -> X
as well as the rightmost startpoint of all your right swaps so far -> Y

Loop through B from left to right

If the first array never contained this element, must be impossible

At each index, see if you can swap right, see if you can swap left
If you can do both, swap right

Condition to swap right at index i:
max(X, Y) < i, >= 1 index j such that A[j] == B[i] and max(X, Y) <= j < i
Take the smallest such j, or do nothing if it doesn't exist

Condition to swap left at index i:
>= i index j such that A[j] == B[i] and max(X, i) <= j, i <= j
Take the smallest such j, or do nothing if it doesn't exist

If nothing has been done, it is impossible

At the end just print out the values in the correct order
'''

import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())

left = []
right = []

arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

indices = [[] for _ in range(3 * 10 ** 5 + 1)]

for i in range(n):
    indices[arr[i]].append(i)

a = -1 # Rightmost r in swipe lefts
b = -1 # Rightmost l in swipe rights

for i in range(n):
    if not indices[brr[i]]:
        print('NO')
        sys.exit()

    if i == 0:
        left.append([i, indices[brr[i]][0]])
        a = indices[brr[i]][0]
        continue

    # Try to swipe right
    if max(a, b) < i and indices[brr[i]][0] < i:

        lo = bisect_left(indices[brr[i]], max(a, b))

        if lo < len(indices[brr[i]]) and indices[brr[i]][lo] < i:
            b = indices[brr[i]][lo]
            right.append([b, i])
            continue

    # Try to swipe left
    if indices[brr[i]][-1] >= i:

        lo = bisect_left(indices[brr[i]], max(a, i))

        if lo < len(indices[brr[i]]) and indices[brr[i]][lo] >= i:
            a = indices[brr[i]][lo]
            left.append([i, a])
            continue

    print('NO')
    sys.exit()

print('YES')
print(len(left) + len(right))

for i in left:
    print('L', *i)

for i in right[::-1]:
    print('R', *i)
