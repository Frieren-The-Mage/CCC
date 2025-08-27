'''
https://dmoj.ca/problem/ccc00s3
Painful and boring problem
But I actually thought it was useful, since I got better at implementation
'''

from collections import deque

url_indx = {}
indx = 0

adj_list = [[] for _ in range(100 + 1)]

is_end = lambda s: "</HTML>" in s

def web_page():
    global indx

    s = input()

    if s not in url_indx.keys():
        url_indx[s] = indx
        indx += 1

    while True:
        l = input()

        for i in range(len(l)):
            if l[i: i + 9] == "<A HREF=\"":
                cur = ''
                j = i + 9

                while l[j] != '\"' and j < len(l):
                    cur += l[j]
                    j += 1

                if cur not in url_indx.keys():
                    url_indx[cur] = indx
                    indx += 1

                print(f"Link from {s} to {cur}")
                adj_list[url_indx[s]].append(url_indx[cur])

        if is_end(l):
            break

for i in range(int(input())):
    web_page()

def bfs(start):
    visited = [False] * (100 + 1)
    visited[start] = True

    queue = deque([start])

    while queue:
        node = queue.popleft()

        for v in adj_list[node]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    return visited

while True:
    a = input()

    if a == 'The End':
        break

    b = input()
    x, y = url_indx[a], url_indx[b]

    if bfs(x)[y]:
        print(f"Can surf from {a} to {b}.")

    else:
        print(f"Can't surf from {a} to {b}.")
