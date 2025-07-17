from collections import deque
import sys
input = sys.stdin.readline
queue = deque()

N = int(input())
for i in range(N):
    order = input().strip()
    
    if order == '3':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif order == '4':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif order == '5':
        print(len(queue))
    elif order == '6':
        if queue:
            print(0)
        else:
            print(1)
    elif order == '7':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif order == '8':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        o, x = order.split()
        if o == '1':
            queue.appendleft(int(x))
        elif o == '2':
            queue.append(int(x))