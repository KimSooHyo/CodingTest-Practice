import sys
from collections import deque
input = sys.stdin.readline

queue = deque()

N = int(input())
num_list = list(map(int, input().split()))
balloons = deque((i + 1, num) for i, num in enumerate(num_list))
order = []

while balloons:
    idx, move = balloons.popleft()
    order.append(idx)
    
    if not balloons:
        break
    
    if move > 0:
        balloons.rotate(-(move-1))
    else:
        balloons.rotate(-move)
        
print(*order)