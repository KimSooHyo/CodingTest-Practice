import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = []
distance = [[[999] * M for _ in range(N)] for _ in range(H)]

for _ in range(H):
    l = [list(map(int, input().split())) for _ in range(N)]
    graph.append(l)

dz = [1,-1,0,0,0,0]
dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]
day = 0

queue = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 1:
                queue.append((z,y,x,0))
                
while queue:
    cz, cy, cx, dist = queue.popleft()
    day = max(day, dist)
        
    for i in range(6):
        nz = cz + dz[i]
        ny = cy + dy[i]
        nx = cx + dx[i]
            
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
            if graph[nz][ny][nx] == 0:
                queue.append((nz, ny, nx, dist+1))
                graph[nz][ny][nx] = 1
        
for z in range(H):
    for y in range(N):
        if 0 in graph[z][y]:
            print(-1)
            sys.exit(0)
                     
print(day)