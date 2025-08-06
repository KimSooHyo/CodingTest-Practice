import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False] *m for _ in range(n)]

dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]
dist = 0

def bfs(x, y):
    queue = deque()
    queue.append((x,y, 1))
    visited[y][x] = True
    
    while queue:
        cx, cy, dist = queue.popleft()
        if cx == m-1 and cy == n-1:
            return dist
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n:
            
                if not visited[ny][nx] and graph[ny][nx] == '1':
                    visited[ny][nx] = True
                    queue.append((nx, ny, dist +1))
    

print(bfs(0, 0))
