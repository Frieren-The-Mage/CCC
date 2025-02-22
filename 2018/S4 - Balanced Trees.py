#https://dmoj.ca/problem/ccc18s4

from math import floor, sqrt

n = int(input())

# Pretty easy O(N) solution, but sub-linear requires some math factoring knowledge
# Instead of choosing the k value, loop through each unique subtree weights
# O(sqrt N) to loop
# No idea what the time complexity is

memo = {}

def num(val):
    # Finds the number of perfectly balanced trees with weight val
    if val in memo.keys():
        return memo[val]

    if val == 1:
        # Must be a single node
        memo[val] = 1
        return 1

    ans = 0

    for i in range(1, floor(sqrt(val)) + 1):
        # For each i, i is the maximum value each subtree can have

        r1 = val // i
        l1 = floor(val / (i + 1) + 1)

        r2 = val // (val // i)
        l2 = floor(val / (val // i + 1) + 1)

        if i == 1:
            # can only choose 1, not val
            ans += (r1 - l1 + 1) * num(i)

        elif i == val // i:
            # elif statement is important to not over count
            ans += (r1 - l1 + 1) * num(i)

        else:
            ans += (r1 - l1 + 1) * num(i)
            ans += (r2 - l2 + 1) * num(val // i)

    memo[val] = ans
    return ans

print(num(n))
