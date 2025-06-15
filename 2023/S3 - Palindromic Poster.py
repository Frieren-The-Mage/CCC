
# https://dmoj.ca/problem/ccc23s3
'''
Actually a really enjoyable problem, solved in roughly 70 minutes

The basic idea for general cases is to:
    - Have all the row palindromes on the topmost rows, filled with 'a'
    - Have all the col palindromes on the leftmost cols, filled with 'a'

Then, fill everything else with 'b'.
Example: (5, 4, 2, 2)
    a a a a a
    a a a a a
    a a b b b
    a a b b b
    a a b b b

However, the first edge case is when R = 0. To deal with this, add an extra layer
Example: (5, 4, 0, 2)
    a a b b b
    a a c c c
    a a c c c
    a a c c c
    a a c c c
A similar idea can be used if C = 0.

The next edge case is if R = N or C = M.
You would deal with them like so:

(5, 6, 5, 4)
a a b b a a
a a c c a a
a a c c a a
a a c c a a
a a c c a a

'''

import sys

n, m, r, c = map(int, input().split())

grid = [['!'] * m for _ in range(n)]

if r == c == 0:
    for i in range(n):
        for j in range(m):
            grid[i][j] = 'abc'[(i + j) % 3]

    for i in grid:
        print(''.join(i))
    sys.exit()

if r == n:
    if c % 2 == 1 and m % 2 == 0:
        print('IMPOSSIBLE')
        sys.exit()

    if c % 2 == 1:
        for i in range(n):
            grid[i][m // 2] = 'a'

    for j in range(c // 2):
        for i in range(n):
            grid[i][j] = 'a'
            grid[i][-1 - j] = 'a'

    for j in range(m):
        if grid[0][j] != 'a':
            assert grid[0][j] == '!'

            grid[0][j] = 'b'
            for i in range(1, n):
                grid[i][j] = 'c'

    for i in grid:
        print(''.join(i))
    sys.exit()

if c == m:
    if r % 2 == 1 and n % 2 == 0:
        print('IMPOSSIBLE')
        sys.exit()

    if r % 2 == 1:
        for j in range(m):
            grid[n // 2][j] = 'a'

    for i in range(r // 2):
        for j in range(m):
            grid[i][j] = 'a'
            grid[-1 - i][j] = 'a'

    for i in range(n):
        if grid[i][0] != 'a':

            grid[i][0] = 'b'
            for j in range(1, m):
                grid[i][j] = 'c'

    for i in grid:
        print(''.join(i))
    sys.exit()

for i in range(n):
    for j in range(m):
        if i < r or j < c:
            grid[i][j] = 'a'
            continue

        if r != 0 and c != 0:
            grid[i][j] = 'b'
            continue

        if r == 0 and i == 0 or c == 0 and j == 0:
            grid[i][j] = 'b'
            continue

        grid[i][j] = 'c'

for i in grid:
    print(''.join(i))
