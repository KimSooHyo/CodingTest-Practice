import sys
input = sys.stdin.readline

"""
2행 이라는 것에 집중

1. 위 스티커를 고른 경우 -> 다음엔 아래를 고르거나 고르지 않음
2. 아래 스티커 -> 위/고르지 않음
3. 고르지 않는 이유는? 전에 고른 것과 같은 행의 스티커를 고르려고
"""

T = int(input())
for _ in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    
    if n > 1:
        dp[0][1] = sticker[0][1] + dp[1][0]
        dp[1][1] = sticker[1][1] + dp[0][0]
    
    for i in range(2, n):
        dp[0][i] = sticker[0][i] + max(dp[1][i-1], dp[1][i-2], dp[0][i-2])
        dp[1][i] = sticker[1][i] + max(dp[0][i-1], dp[0][i-2], dp[1][i-2])
        
    print(max(dp[0][n-1], dp[1][n-1]))