#https://dmoj.ca/problem/ccc11s5

# Can represent the states of the lights using bitmask
# BFS to find the shortest path to 0
# Don't consider turning on lights that are not adjacent to on lights

from collections import deque

def do_operation(a):
    # Turns off 4 or more consecutive lights
    s = 0
    cur = 0

    # n + 1 to add a buffer 0 at the end
    for j in range(n + 1):
        bit = a & (1 << j)

        if bit:
            cur += 1

        elif bit == 0 and cur > 0:

            if cur < 4:
                s |= ((1 << cur) - 1) << (j - cur)

            cur = 0

    return s

n = int(input())

mask = 0

for i in range(n):
    mask <<= 1

    x = int(input())

    mask |= x

visited = set()
visited.add(mask)

queue = deque([(mask, 0)])
# mask, dist (dist is num operations)

while queue:
    m, d = queue.popleft()
    #print(str(bin(m))[2:], d)

    if m == 0:
        print(d)
        break

    for k in range(n):

        if k == 0:
            if (m & (1 << k)) == 0 and m & 1 << (k + 1):
                new_m = do_operation(m | (1 << k))
                if new_m not in visited:
                    visited.add(new_m)
                    queue.append((new_m, d + 1))
            continue

        if (m & (1 << k)) == 0 and (m & (1 << (k - 1)) or m & (1 << (k + 1))):
            new_m = do_operation(m | (1 << k))
            # The light is off, adj to an on light
            # and we have not visited it yet
            if new_m not in visited:
                visited.add(new_m)
                queue.append((new_m, d + 1))
