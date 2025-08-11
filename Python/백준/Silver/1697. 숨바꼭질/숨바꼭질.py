from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
Max = 100000
visited = [False] * (Max+1)

queue = deque()
queue.append((N, 0))
visited[N] = True

while queue:
    pos, time = queue.popleft()
    
    if pos == K:
        print(time)
        break
    
    for next in (pos-1, pos+1, pos*2):
        if 0 <= next <= Max and not visited[next]:
            visited[next] = True
            queue.append((next, time+1))