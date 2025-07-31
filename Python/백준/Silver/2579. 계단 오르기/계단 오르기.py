import sys
input = sys.stdin.readline

n = int(input())
stairs = []
for _ in range(n):
    line = input()
    if line.strip():  # 빈 줄 방지
        stairs.append(int(line))

# stairs 길이가 부족할 경우 대비
if n != len(stairs):
    n = len(stairs)

if n == 0:
    print(0)
elif n == 1:
    print(stairs[0])
elif n == 2:
    print(stairs[0] + stairs[1])
else:
    dp = [0] * n
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, n):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

    print(dp[-1])
