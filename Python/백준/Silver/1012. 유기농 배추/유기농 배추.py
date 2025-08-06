import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

t = int(input())

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visited[y][x] = True
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny))
    
    
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
        
    cnt = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1 and not visited[y][x]:
                bfs(x, y)
                cnt += 1
    
    print(cnt)