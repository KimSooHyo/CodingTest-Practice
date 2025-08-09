import sys
input = sys.stdin.readline
MOD = 1000000000

N = int(input().strip())

# 초기 (길이 1)
dp = [0]*10
for d in range(1, 10):
    dp[d] = 1

for _ in range(2, N+1):
    ndp = [0]*10
    ndp[0] = dp[1] % MOD
    ndp[9] = dp[8] % MOD
    for d in range(1, 9):
        ndp[d] = (dp[d-1] + dp[d+1]) % MOD
    dp = ndp

print(sum(dp) % MOD)
