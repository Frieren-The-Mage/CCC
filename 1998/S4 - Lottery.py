
'''
https://dmoj.ca/problem/ccc98s4
Fairly intuitive recursion / stack logic
'''


def solve():
    ops = input().split()
    
    # Contains all multiplication surrounded by ().
    arr = []

    for i, val in enumerate(ops):
        arr.append(val)
    
        # Pop the last 3, and append them with parenthesis as 1 element
        if i != 0 and ops[i - 1] == 'X':
            b = arr.pop()
            arr.pop()
            a = arr.pop()

            arr.append(f'({a} X {b})')
    
    # Contains the actual answer
    ans = []

    for i, val in enumerate(arr):
        ans.append(val)
        
        # Pop the last 3, and append them with parenthesis as 1 element
        if i != 0 and (arr[i - 1] == '-' or arr[i - 1] == '+'):
            b = ans.pop()
            o = ans.pop()
            a = ans.pop()

            ans.append(f"({a} {o} {b})")
    
    # [1:-1] because there is an extra () on the entire expression.
    print(' '.join(ans)[1:-1])

t = int(input())
for _ in range(t):
    solve()

    if _ != t - 1:
        print()
