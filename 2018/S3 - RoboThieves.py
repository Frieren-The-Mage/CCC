from collections import deque

#https://dmoj.ca/problem/ccc18s3
# Terrible problem, really boring and annoying
# Without the comments section, I would have been stuck on this for > 3 days
# Problem statement sounds kind of cool though

n, m = map(int, input().split())

grid = [list(input()) for _ in range(n)]

camera = [[False] * m for _ in range(n)]
# Define camera[i][j] if (i, j) can be seen by a conveyor

def update_camera(x, y):

    camera[x][y] = True

    up = x
    while up >= 0:
        if grid[up][y] == 'W':
            # No more scope
            break

        elif grid[up][y] in 'LRUD':
            # conveyors are elevated
            up -= 1
            continue

        camera[up][y] = True
        up -= 1

    down = x
    while down < n:
        if grid[down][y] == 'W':
            # No more scope
            break

        elif grid[down][y] in 'LRUD':
            # conveyors are elevated
            down += 1
            continue

        camera[down][y] = True
        down += 1

    left = y
    while left >= 0:
        if grid[x][left] == 'W':
            # No more scope
            break

        elif grid[x][left] in 'LRUD':
            # conveyors are elevated
            left -= 1
            continue

        camera[x][left] = True
        left -= 1

    right = y
    while right < m:
        if grid[x][right] == 'W':
            # No more scope
            break

        elif grid[x][right] in 'LRUD':
            # conveyors are elevated
            right += 1
            continue

        camera[x][right] = True
        right += 1

# Find cameras and update camera
# Also find the starting location
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'C':
            update_camera(i, j)

        if grid[i][j] == 'S':
            start_x = i
            start_y = j

indices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dist = [[float('inf')] * m for _ in range(n)]

def bfs():

    if camera[start_x][start_y]:
        return

    visited = [[False] * m for _ in range(n)]
    visited[start_x][start_y] = True

    queue = deque([(start_x, start_y, 0)])

    while queue:
        node_x, node_y, d = queue.popleft()

        dist[node_x][node_y] = min(dist[node_x][node_y], d)

        # Forced to go in locations
        if grid[node_x][node_y] in 'LRUD':
            if grid[node_x][node_y] == 'L':
                new_x = node_x
                new_y = node_y - 1

            if grid[node_x][node_y] == 'R':
                new_x = node_x
                new_y = node_y + 1

            if grid[node_x][node_y] == 'U':
                new_x = node_x - 1
                new_y = node_y

            if grid[node_x][node_y] == 'D':
                new_x = node_x + 1
                new_y = node_y

            if (0 <= new_x < n and 0 <= new_y < m and
                    not (visited[new_x][new_y]) and
                    not (camera[new_x][new_y]) and
                    grid[new_x][new_y] != 'W'):

                visited[new_x][new_y] = True

                # 0/1 BFS
                if grid[new_x][new_y] in 'LRUD':
                    queue.appendleft((new_x, new_y, d))

                else:
                    queue.append((new_x, new_y, d))

            continue

        for change_x, change_y in indices:
            new_x = node_x + change_x
            new_y = node_y + change_y

            if (0 <= new_x < n and 0 <= new_y < m and
                    not(visited[new_x][new_y]) and
                    not(camera[new_x][new_y]) and
                    grid[new_x][new_y] != 'W'):

                visited[new_x][new_y] = True

                # 0/1 BFS
                if grid[new_x][new_y] in 'LRUD':
                    queue.appendleft((new_x, new_y, d + 1))

                else:
                    queue.append((new_x, new_y, d + 1))

bfs()

for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':

            if dist[i][j] == float('inf'):
                print(-1)

            else:
                print(dist[i][j])

