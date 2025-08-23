'''
https://dmoj.ca/problem/ccc06j5
Just pure implementation, nothing else to say
That moment when your code is wrong because you messed up the original configuration
'''

info = input().split()

# 0 = empty, 1 = black, 2 = white
grid = [[0] * (8 + 1) for _ in range(8 + 1)]

indices = [(0, 1), (0, -1), (1, 0), (-1, 0),
           (1, 1), (1, -1), (-1, 1), (-1, -1)]

if info[0] == 'a':
    grid[4][4] = 2
    grid[5][5] = 2
    grid[4][5] = 1
    grid[5][4] = 1

elif info[0] == 'b':
    for i in range(1, 8 + 1):
        grid[i][i] = 1
        grid[i][8 - i + 1] = 2

else:
    for i in range(1, 8 + 1):
        for j in range(3, 4 + 1):
            grid[i][j] = 1
            grid[i][j + 2] = 2

def move(x, y, bit):
    grid[x][y] = bit

    for cx, cy in indices:
        nx = x + cx
        ny = y + cy
        switch = []
        flag = False
        blank = False

        while 1 <= nx <= 8 and 1 <= ny <= 8:
            if grid[nx][ny] == 3 ^ bit and not blank:
                switch.append((nx, ny))

            if grid[nx][ny] == bit:
                flag = True
                break

            if grid[nx][ny] == 0:
                blank = True

            nx += cx
            ny += cy

        if flag:
            for i, j in switch:
                grid[i][j] ^= 3

n = int(info[1])
info = list(map(int, info[2:]))
info = [[info[i], info[i + 1]] for i in range(0, len(info), 2)]

bit = 1

for x, y in info:
    move(x, y, bit)
    bit ^= 3

black = sum(i.count(1) for i in grid)
white = sum(i.count(2) for i in grid)

print(black, white)
