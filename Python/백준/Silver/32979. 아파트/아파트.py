import sys
from collections import deque

n = int(sys.stdin.readline())
t = int(sys.stdin.readline())

queue = deque()
result = []

list = sys.stdin.readline().strip().split()
for l in list:
    queue.append(l)
time = sys.stdin.readline().strip().split()
for b in time:
    
    for j in range(int(b)-1):
        s = queue.popleft()
        queue.append(s)
        
    result.append(queue[0])
    
print(" ".join(result))    
