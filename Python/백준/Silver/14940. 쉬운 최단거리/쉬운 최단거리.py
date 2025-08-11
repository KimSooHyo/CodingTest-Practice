import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

distance = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 시작점 찾기
found = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            startx, starty = j, i
            found = True
    if found:
        break

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
distance[starty][startx] = 0

# BFS
def bfs(x, y, dist):
    queue = deque()
    queue.append((x, y, dist))
    visited[y][x] = True
    
    while queue:
        cx, cy, new_dist = queue.popleft()
        distance[cy][cx] = new_dist
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and graph[ny][nx] != 0:
                queue.append((nx, ny, new_dist + 1))
                visited[ny][nx] = True

bfs(startx, starty, 0)

# 갈 수 없는 땅은 0으로
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            distance[i][j] = 0

# 출력
for row in distance:
    print(*row)
