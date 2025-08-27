
import sys

'''
https://dmoj.ca/problem/ccc01s5
Simple recursive problem, not much to say
'''

m = int(input())
n = int(input())

arr = [[input() for _ in range(n)], [input() for _ in range(n)]]

sequence = lambda indx, indices: ''.join([arr[indx][i - 1] for i in indices])

def solve(length):
    if length == 1:
        cur = [[i] for i in range(1, n + 1)]
        for i in range(1, n + 1):
            if sequence(0, [i]) == sequence(1, [i]):
                print(length)
                print(i)
                sys.exit()
        return cur

    prev = solve(length - 1)
    cur = []
    for i in range(1, n + 1):
        for each in prev:
            if sequence(0, each + [i]) == sequence(1, each + [i]):
                print(length)
                print('\n'.join(map(str, each + [i])))
                sys.exit()

            cur.append(each + [i])
    return cur

solve(m - 1)
print("No solution.")
