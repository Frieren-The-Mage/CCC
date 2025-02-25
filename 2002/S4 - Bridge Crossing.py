#https://dmoj.ca/problem/ccc02s4

# We observe how bounds are small,
# which implies not O(1) state transition.

m = int(input()) # maximum group length
q = int(input()) # length of queue

names = []
# names[i] = name of ith person

times = []
# times of ith person

for i in range(q):
    n = input()
    t = int(input())

    names.append(n)
    times.append(t)

def time_needed(arr):
    # Finds the time required for a certain configuration
    ans = 0

    for i in arr:
        s = 0

        for j in i:
            s = max(s, times[j])

        ans += s

    if ans == 0:
        # So we don't accept [] as the best
        return float('inf')

    return ans

dp = [[] for _ in range(q)]
# Define dp[i] = configuration of min time for first i people
# Stores the indices of the people

# Base Case
dp[0] = [ [0] ]

for i in range(1, q):

    if i - (m - 1) <= 0:
        # Can form a group with all people
        dp[i] = [ [j for j in range(i + 1)] ]

    for prev in range(max(i - m, i - q, 0), i):
        # Finds the most optimal last group
        # Important for max(i - m, i - q, 0)
        # instead of max(i - q, 0) because q can be really big compared to m

        # We don't need to consider prev = -1 because we already considered the entire group
        # prev + 1 to i inclusive is the last group

        cur = dp[prev] + [ [j for j in range(prev + 1, i + 1)] ]

        dp[i] = min(dp[i], cur, key=lambda x: time_needed(x))

tot = 0
ans = [[] for _ in range(len(dp[-1]))]

for i in range(len(dp[-1])):
    cur = 0
    for j in dp[-1][i]:
        cur = max(cur, times[j])
        ans[i].append(names[j])

    tot += cur

print(f"Total Time: {tot}")
for i in ans:
    print(*i)
