
'''
https://dmoj.ca/problem/ccc08s4
Relatively simple recursion problem
For each set of cards, check all possible pairs of valid operations
Didn't know you could reorder the card order...
'''


def solve(arr):

    # Base Case, no more operations to do
    if len(arr) == 1:
        return [arr[0]]

    # Store all states
    cur = []

    # Loop through all valid pairs
    for i in range(len(arr)):
        for j in range(len(arr)):

            if i == j:
                continue
            a = arr[i]
            b = arr[j]

            # Call recursive function
            cur += solve([a + b] + [arr[k] for k in range(len(arr)) if k != i and k != j])
            cur += solve([a - b] + [arr[k] for k in range(len(arr)) if k != i and k != j])
            cur += solve([a * b] + [arr[k] for k in range(len(arr)) if k != i and k != j])

            # Special condition in order to call function
            if b != 0 and a % b == 0:
                cur += solve([a // b] + [arr[k] for k in range(len(arr)) if k != i and k != j])

    # Return state
    return cur

for _ in range(int(input())):
    vals = [int(input()) for i in range(4)]

    ans = solve(vals)

    # Filer values above 24
    ans = list(filter(lambda x: x <= 24, ans))

    print(max(ans))
