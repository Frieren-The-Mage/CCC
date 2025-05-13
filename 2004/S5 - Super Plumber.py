'''
https://dmoj.ca/problem/ccc04s5
Relatively Simple DP Problem
For each cell, we consider going up and going down
'''

def solve(n, m):
    grid = [list(input().replace('.', '0')) for _ in range(n)]

    # Define dp[i][j] = max value from (i, j) to (n - 1, m - 1)
    dp = [[-float('inf')] * m for _ in range(n)]

    # Base Case
    dp[-1][-1] = int(grid[-1][-1])

    for row in range(n - 2, -1, -1):

        if grid[row][-1] == '*':
            continue

        dp[row][-1] = int(grid[row][-1]) + dp[row + 1][-1]

    for col in range(m - 2, -1, -1):

        # Go Down
        if grid[-1][col] != '*':
            dp[-1][col] = int(grid[-1][col]) + dp[-1][col + 1]

        for row in range(n - 2, -1, -1):
            if grid[row][col] == '*':
                continue

            dp[row][col] = int(grid[row][col]) + dp[row][col + 1]
            running = int(grid[row][col])

            for next in range(row + 1, n):

                if grid[next][col] == '*': break
                running += int(grid[next][col])
                dp[row][col] = max(dp[row][col], running + dp[next][col + 1])

        # Go Up
        if grid[0][col] != '*':
            dp[0][col] = max(dp[0][col], int(grid[0][col]) + dp[0][col + 1])

        for row in range(1, n):
            if grid[row][col] == '*':
                continue

            dp[row][col] = max(dp[row][col], int(grid[row][col]) + dp[row][col + 1])
            running = int(grid[row][col])

            for next in range(row - 1, -1, -1):

                if grid[next][col] == '*': break
                running += int(grid[next][col])
                dp[row][col] = max(dp[row][col], running + dp[next][col + 1])

    print(dp[-1][0])

while True:
    n, m = map(int, input().split())

    if n == m == 0:
        break

    solve(n, m)
