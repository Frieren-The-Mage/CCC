#https://dmoj.ca/problem/ccc05s3
# Simple operations on 2D Arrays

def tensor(a1, a2):

    # Multiplies through
    def update(arr, i, j, r, c, val, orig):
        for ii in range(i, i + r):
            for jj in range(j, j + c):
                arr[ii][jj] = orig[ii - i][jj - j] * val


    res = [[0] * (len(a1[0]) * len(a2[0])) for _ in range(len(a1) * len(a2))]

    for i in range(0, len(res), len(a2)):
        for j in range(0, len(res[0]), len(a2[0])):

            # For each square of same dimensions as the second array,
            # Find multiplication value and update the matrix
            mult = a1[i // len(a2)][j // (len(a2[0]))]
        
            update(res, i, j, len(a2), len(a2[0]), mult, a2)

    return res

n = int(input())

cur = None

for i in range(n):

    r, c = map(int, input().split())

    mat = [list(map(int, input().split())) for _ in range(r)]

    if cur is None:
        cur = mat
        continue

    cur = tensor(cur, mat)

# Extract Answer
mx = float('-inf')
mn = float('inf')

mx_row = float('-inf')
mn_row = float('inf')

mx_col = float('-inf')
mn_col = float('inf')

for i in cur:
    mx = max(mx, max(i))
    mn = min(mn, min(i))

    mx_row = max(mx_row, sum(i))
    mn_row = min(mn_row, sum(i))
    
# Too lazy for another method
cols = [[cur[i][j] for i in range(len(cur))] for j in range(len(cur[0]))]

for i in cols:
    mx_col = max(mx_col, sum(i))
    mn_col = min(mn_col, sum(i))

print(mx)
print(mn)
print(mx_row)
print(mn_row)
print(mx_col)
print(mn_col)
