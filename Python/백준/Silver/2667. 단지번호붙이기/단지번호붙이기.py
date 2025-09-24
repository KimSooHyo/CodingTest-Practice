from collections import deque
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
grid = [[] for _ in range(n)]
for i in range(n):
    grid[i] = list(input().strip())
answer = []

def bfs(y, x):
    queue = deque()
    queue.append((y,x))
    grid[y][x] = '0'
    cnt = 1
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < n:
                if grid[ny][nx] == '1':
                    queue.append((ny, nx))
                    grid[ny][nx] = '0'
                    cnt += 1
    
    return cnt

for i in range(n):
    for j in range(n):
        if grid[i][j] == '1':   # (i,j) 순서 주의
            answer.append(bfs(i, j))

print(len(answer))             # 총 단지 수
for x in sorted(answer):       # 오름차순 출력
    print(x)
            