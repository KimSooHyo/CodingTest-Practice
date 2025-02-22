from math import sqrt

n = int(input())

def solve():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    ans = 0

    dist = sqrt((x1-x2)**2 + (y1-y2)**2)
    diff = abs(r1 - r2)
    
    if diff == 0 and dist == 0:
        ans = -1
    
    elif r1+r2 == dist or diff == dist:
        ans = 1
    
    elif diff < dist < r1+r2:
        ans = 2
    
    print(ans)
    
    
for _ in range(n):
    solve()