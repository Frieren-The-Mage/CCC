
'''
https://dmoj.ca/problem/ccc06s4
Pretty easy and straightforward problem
Looks a bit annoying, but is actually not that bad
'''

def solve(n):
    grid = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

    # Check if x and y are in G, so is f(x, y)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if not (1 <= grid[i][j] <= n):
                print('no')
                return

    # Check Associativity
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):

                if grid[i][grid[j][k]] != grid[grid[i][j]][k]:
                    print('no')
                    return

    # Function to check if a value is the identity
    def is_identity(val):
        ans = True
        for i in range(1, n + 1):
            ans = ans and (grid[i][val] == i and grid[val][i] == i)
        return ans

    # Find identity
    iden = None

    for i in range(1, n + 1):
        if is_identity(i):
            iden = i
            break

    if iden is None:
        print('no')
        return

    # Find inverse for each element
    for i in range(1, n + 1):
        inv = False

        for j in range(1, n + 1):
            if grid[i][j] == iden:
                inv = True
                break

        if not inv:
            print('no')
            return

    print('yes')


while True:
    n = int(input())

    if n == 0:
        break

    solve(n)
