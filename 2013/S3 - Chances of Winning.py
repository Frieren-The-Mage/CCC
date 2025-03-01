#https://dmoj.ca/problem/ccc13s3
# Simple backtracking idea

t = int(input()) - 1

# Keep track of the games left to play
games = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

scores = [0] * 4 # Scores of the players, 0-indexed

g = int(input())

for i in range(g):
    a, b, sa, sb = map(int, input().split())

    a -= 1
    b -= 1

    if a > b:
        a, b = b, a
        sa, sb = sb, sa

    # Update information after game is played
    games.remove((a, b))

    if sa > sb:
        scores[a] += 3

    elif sa < sb:
        scores[b] += 3

    else:
        scores[a] += 1
        scores[b] += 1

n = len(games)

# Backtrack
def solve(i):
    global tot

    if i == n:
        return (scores[t] > scores[(t + 1) % 4] and
                scores[t] > scores[(t + 2) % 4] and
                scores[t] > scores[(t + 3) % 4])

    a, b = games[i]
    cur = 0

    scores[a] += 3
    cur += solve(i + 1)
    scores[a] -= 3

    scores[b] += 3
    cur += solve(i + 1)
    scores[b] -= 3

    scores[a] += 1
    scores[b] += 1
    cur += solve(i + 1)
    scores[a] -= 1
    scores[b] -= 1

    return cur

tot = solve(0)
print(tot)
