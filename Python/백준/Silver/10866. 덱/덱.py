from collections import deque
import sys

queue = deque()

n = int(sys.stdin.readline())

for i in range(n):
    order = sys.stdin.readline().strip()
    
    if order == 'pop_front':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif order == 'pop_back':
        if not queue:
            print(-1)
        else:
            print(queue.pop())
            
    elif order == 'size':
        print(len(queue))
        
    elif order == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif order == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
            
    else:
        o, n = order.split()
        if o == 'push_front':
            queue.appendleft(n)
        else:
            queue.append(n)