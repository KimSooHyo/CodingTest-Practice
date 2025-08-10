import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(x, y):
    graph[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1:
            dfs(nx, ny)

T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(T):
    M,N,K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    
    cnt = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                dfs(x, y)
                cnt += 1
    print(cnt)