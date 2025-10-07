
'''
https://dmoj.ca/problem/ccc06s3

Was learning some Geoemetry because recent AtCoder had a geo problem
Figured out you could represent the polygons as individual line segments myself,
for the intersection part, I read CPH, but I coded it myself
The idea is to use vectors for a point (x, y) to get cross product,
then use cross products to determine if a point is on a line, to the left, or to the right
After that 2 line segments intersect if they overlap in infinite points, at exactly an endpoint,
or line 1's points are on opposite sides of line 2 and vice versa.
'''


def subtract(p1, p2):
    return [p1[0] - p2[0], p1[1] - p2[1]]

def cross_product(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]

def line_val(s1, s2, p):
    return cross_product(subtract(p, s1), subtract(p, s2))

def intersect(p1, p2, p3, p4):

    if p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4:
        return True

    if line_val(p1, p2, p3) == 0 and line_val(p1, p2, p4) == 0:
        arr = sorted([p1, p2, p3, p4])

        if arr[:2] == sorted([p1, p2]) or arr[:2] == sorted([p3, p4]):
            return False

        return True

    if line_val(p1, p2, p3) > 0 and line_val(p1, p2, p4) > 0 or line_val(p1, p2, p3) < 0 and line_val(p1, p2, p4) < 0:
        return False

    if line_val(p3, p4, p1) > 0 and line_val(p3, p4, p2) > 0 or line_val(p3, p4, p1) < 0 and line_val(p3, p4, p2) < 0:
        return False

    return True

x1, y1, x2, y2 = map(int, input().split())
p1 = [x1, y1]
p2 = [x2, y2]

ans = 0

for _ in range(int(input())):
    info = list(map(int, input().split()))

    points = [[info[i], info[i + 1]] for i in range(1, 2 * info[0], 2)]
    points.append(points[0])

    cur = False

    for i in range(info[0]):
        cur = cur or intersect(p1, p2, points[i], points[i + 1])

    ans += cur

print(ans)
