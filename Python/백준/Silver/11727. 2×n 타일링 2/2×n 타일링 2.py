import sys
input =sys.stdin.readline

n = int(input())

dp = [0] * (n+2)
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007

print(dp[n])
