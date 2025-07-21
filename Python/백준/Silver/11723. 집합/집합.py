import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    order = input().strip()
    
    if order == 'all':
        S = set(i for i in range(1, 21))
    elif order == 'empty':
        S = set()
    else:
        o, x = order.split()
        x = int(x)
        if o == 'add':
            S.add(x)
        elif o == 'remove':
            if x in S:
                S.remove(x)
        elif o == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif o == 'toggle':
            if x in S:
                S.remove(x)
            else:
                S.add(x)