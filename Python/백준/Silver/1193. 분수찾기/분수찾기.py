X = int(input())

n = 1
while n * (n + 1) // 2 < X:
    n += 1

prev_sum = (n - 1) * n // 2
pos = X - prev_sum  # 현재 대각선에서의 위치

if n % 2 == 0:  # 짝수 대각선: 아래 → 위
    numerator = pos
    denominator = n - pos + 1
else:           # 홀수 대각선: 위 → 아래
    numerator = n - pos + 1
    denominator = pos

print(f"{numerator}/{denominator}")
