from collections import deque
import sys
input = sys.stdin.readline
queue = deque()

N = int(input())
for i in range(N):
    order = input().strip()
    
    if order == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif order == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        o, x = order.split()
        queue.append(int(x))