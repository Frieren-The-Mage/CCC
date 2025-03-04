#https://dmoj.ca/problem/ccc20s4
# Learned a really cool technique to deal with circular problems
# Implementation is annoying as usual
# Logic is a bit difficult to visualize at first, but not that bad
# Could've decreased code length, but I didn't have any bugs

seating = input() * 2 # Double string for wrapping around
n = len(seating)

num_a = seating.count('A') // 2
num_b = seating.count('B') // 2
num_c = seating.count('C') // 2

# Since the number of groups that wrap around is at most one

psa = [[0, 0, 0]]
# A's, B's, C's

for i in range(n):
    psa.append(psa[-1].copy())

    psa[-1][0] += seating[i] == 'A'
    psa[-1][1] += seating[i] == 'B'
    psa[-1][2] += seating[i] == 'C'

query = lambda r, l : [psa[r + 1][0] - psa[l][0],
                       psa[r + 1][1] - psa[l][1],
                       psa[r + 1][2] - psa[l][2]]

def left(start):
    tot = 0

    a_l = start
    a_r = start + num_a - 1  # inclusive
    a_region = query(a_r, a_l)

    b_l = (start - num_b) % (n // 2)
    b_r = b_l + num_b - 1
    b_region = query(b_r, b_l)

    c_l = (start + num_a) % (n // 2)
    c_r = c_l + num_c - 1
    c_region = query(c_r, c_l)

    tot += min(a_region[1], b_region[0])
    tot += min(a_region[2], c_region[0])
    tot += min(b_region[2], c_region[1])

    min_ab = min(a_region[1], b_region[0])
    min_ac = min(a_region[2], c_region[0])
    min_bc = min(b_region[2], c_region[1])

    a_region[1] -= min_ab
    b_region[0] -= min_ab

    a_region[2] -= min_ac
    c_region[0] -= min_ac

    b_region[2] -= min_bc
    c_region[1] -= min_bc

    tot += (max(a_region[1], a_region[2]) +
            max(b_region[0], b_region[2]) +
            max(c_region[0], c_region[1]) - max(
                max(a_region[1], a_region[2]),
                max(b_region[0], b_region[2]),
                max(c_region[0], c_region[1])
            ))

    return tot

def right(start):
    tot = 0

    a_l = start
    a_r = start + num_a - 1  # inclusive
    a_region = query(a_r, a_l)

    b_l = (start + num_a) % (n // 2)
    b_r = b_l + num_b - 1
    b_region = query(b_r, b_l)

    c_l = (start - num_c) % (n // 2)
    c_r = c_l + num_c - 1
    c_region = query(c_r, c_l)

    tot += min(a_region[1], b_region[0])
    tot += min(a_region[2], c_region[0])
    tot += min(b_region[2], c_region[1])

    min_ab = min(a_region[1], b_region[0])
    min_ac = min(a_region[2], c_region[0])
    min_bc = min(b_region[2], c_region[1])

    a_region[1] -= min_ab
    b_region[0] -= min_ab

    a_region[2] -= min_ac
    c_region[0] -= min_ac

    b_region[2] -= min_bc
    c_region[1] -= min_bc

    tot += (max(a_region[1], a_region[2]) +
            max(b_region[0], b_region[2]) +
            max(c_region[0], c_region[1]) - max(
                max(a_region[1], a_region[2]),
                max(b_region[0], b_region[2]),
                max(c_region[0], c_region[1])
            ))

    return tot

def num_swaps(start):
    # Finds the minimum number of swaps if start is the starting index for
    # all A's
    return min(left(start), right(start))

ans = float('inf')
for i in range(n // 2):
    ans = min(ans, num_swaps(i))

print(ans)
