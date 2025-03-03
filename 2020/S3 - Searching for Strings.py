#https://dmoj.ca/problem/ccc20s3
# Useful problem to learn hashing
# Logic is pretty simple without hashing
# Every permutation of n has an invariant: Number of characters are the same
# So to see if a string is a permutation of n, simply look at the frequencies of each character
# Fixed size sliding window
# To hash, just polynomial hash it and O(1) update when sliding the window

import sys

n = input()

h = input()

if len(n) > len(h):
    print(0)
    sys.exit()

find_ascii = lambda x: ord(x) - 97 # 0 to 25

target = [0] * 26

for i in n:
    target[find_ascii(i)] += 1

window = [0] * 26

# Polynomial hashing
# h(s) = sum of s[i] * p^(len(n) - n - i) for all i, 0 <= i < len(n)
MOD = 177635683940025046467781066894531
p = 31
hash_val = 0

for i in range(len(n)):
    window[find_ascii(h[i])] += 1
  
    hash_val += (find_ascii(h[i]) + 1) * pow(p, len(n) - 1 - i, MOD)
    hash_val %= MOD

# left and right pointers of window
l = 0
r = len(n) - 1 #inclusive

def is_permutation(a, b):
    ans = True
    for i in range(26):
        ans = ans and a[i] == b[i]
    return ans

distinct_permutations = set()

if is_permutation(window, target):
    distinct_permutations.add(hash_val)

if len(n) == len(h):
    print(len(distinct_permutations))
    sys.exit()

while True:
    # Update window value and hash value
    window[find_ascii(h[l])] -= 1

    hash_val -= (find_ascii(h[l]) + 1) * pow(p, len(n) - 1, MOD)
    hash_val *= p

    l += 1
    r += 1

    window[find_ascii(h[r])] += 1

    hash_val += (find_ascii(h[r]) + 1)
    hash_val %= MOD

    if is_permutation(window, target):
        distinct_permutations.add(hash_val)


    if r == len(h) - 1:
        break

print(len(distinct_permutations))
