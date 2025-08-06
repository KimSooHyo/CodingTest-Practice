import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    graph[i] = list(input().strip())

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visited[y][x] = True
    cnt = 1
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if graph[ny][nx] == '1' and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    queue.append((nx, ny))
                    cnt += 1          
                    
    return cnt

total_cnt = []
for i in range(n):
    for j in range(n):
        if graph[j][i] == '1' and visited[j][i] == False:
            total_cnt.append(bfs(i, j))
        
print(len(total_cnt))
for num in sorted(total_cnt):
    print(num)