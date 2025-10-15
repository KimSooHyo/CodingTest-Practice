import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(N+1) for _ in range(N+1)]
for y in range(1, N+1):
    for x in range(1, N+1):
        dp[y][x] = dp[y-1][x] + dp[y][x-1] - dp[y-1][x-1] + grid[y-1][x-1]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])