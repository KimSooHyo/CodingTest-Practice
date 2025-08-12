import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
queue = deque()
day = 0

zero_cnt = 0
for y in range(N):
    for x in range(M):
        if graph[y][x] == 1:
            queue.append((x, y, 0))
        elif graph[y][x] == 0:
            zero_cnt += 1

if zero_cnt == 0:
    print(0)
    exit()

while queue:
    cx, cy, dist = queue.popleft()
    day = max(day, dist)
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if graph[ny][nx] == 0:
                graph[ny][nx] = 1
                queue.append((nx, ny, dist+1))
                
for y in range(N):
    for x in range(M):
        if graph[y][x] == 0:
            print(-1)
            exit()
            
print(day)