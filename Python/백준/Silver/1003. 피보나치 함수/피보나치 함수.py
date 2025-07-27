import sys
input = sys.stdin.readline

# 최대 40까지 미리 계산
dp = [[0, 0] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]

# dp[n] = dp[n-1] + dp[n-2]
for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]  # 0 출력 횟수
    dp[i][1] = dp[i-1][1] + dp[i-2][1]  # 1 출력 횟수

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n][0], dp[n][1])