n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]

# DP 테이블 초기화
dp = [[0] * n for _ in range(n)]
dp[0][0] = tree[0][0]

# DP 점화식 적용
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i-1][0] + tree[i][0]
        elif j == i:
            dp[i][j] = dp[i-1][i-1] + tree[i][i]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tree[i][j]

# 마지막 줄의 최대값이 답
print(max(dp[n-1]))
