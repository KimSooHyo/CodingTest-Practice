"""
문자열이랑 비교해가면서 더 늦으면 뒤에 놓고 빠르면 앞에 놓고.. 이런식으로?
"""

from collections import deque
import sys

queue = deque()
n = int(sys.stdin.readline())

for i in range(n):
    queue = deque()
    
    m = int(sys.stdin.readline())
    list = sys.stdin.readline().strip().split()
    
    for j in range(m):
        
        if not queue:
            queue.append(list[j])
        else:
            if queue[0] >= list[j]:
                queue.appendleft(list[j])
            else:
                queue.append(list[j])
                    
    print("".join(queue))