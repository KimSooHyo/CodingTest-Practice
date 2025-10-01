from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
area = [list(input().strip()) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x, y, color):
    queue = deque()
    queue.append((x,y,color))
    visited[0][0] = True
    
    while queue:
        cx, cy, c = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                if area[ny][nx] == c:
                    queue.append((nx, ny, area[ny][nx]))
                    visited[ny][nx] = True
                    
first = 0
second = 0
visited = [[False] * N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if visited[y][x] == False:
            bfs(x,y,area[y][x])
            first += 1
            
visited = [[False] * N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if area[y][x] == 'G':
            area[y][x] = 'R'
            
for y in range(N):
    for x in range(N):
        if visited[y][x] == False:
            bfs(x,y,area[y][x])
            second += 1
            
print(first, second)