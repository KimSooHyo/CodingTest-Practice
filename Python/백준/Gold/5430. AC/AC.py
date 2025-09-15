import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    arr = input().strip()[1:-1]
    
    if arr:
        queue = deque(arr.split(','))
    else:
        queue = deque()
    
    flag = 0
    error = False
    for c in p:
        if c == 'R':
            flag ^= 1
        elif c == 'D':
            if not queue:
                error = True
                break
            if flag == 0:
                queue.popleft()
            else:
                queue.pop()
                
    if error:
        print("error")
    else:
        if flag == 1:
            queue.reverse()
        print("[" + ",".join(queue) + "]")