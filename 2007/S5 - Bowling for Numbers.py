#https://dmoj.ca/problem/ccc07s5

# Pretty normal DP question
# Guess the states based on input constraints
# The fact that it's a DP question might give away the approach


import sys
from itertools import accumulate
input = sys.stdin.readline

def solve(n: int, k: int, w: int, arr: list[int]):

    # Faster sum calculations
    psa = [0] + list(accumulate(arr))
    query = lambda l, r: psa[r + 1] - psa[l]


    dp = [[0] * (k + 1) for _ in range(n)]
    # Define dp[i][j] = maximum value you can get with
    # first i pins using j balls

    # Base Case
    # dp[any_row][0] = 0

    for i in range(n):
        for j in range(1, k + 1):

            if i < w:
                # Number of pins is less than width, can hit all pins
                dp[i][j] = query(0, i)

            else:
                # If the next ball is rightmost or not
                dp[i][j] = max(dp[i - 1][j],
                               dp[i - w][j - 1] + query(i - (w - 1), i))

    return dp[-1][-1]


t = int(input())
for i in range(t):
    n, k, w = map(int, input().split())

    nums = [int(input()) for _ in range(n)]

    print(solve(n, k, w, nums))
