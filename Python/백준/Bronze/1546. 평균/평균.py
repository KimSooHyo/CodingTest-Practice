n = int(input())
scores = [0] * n
scores = list(map(int, input().split()))

# 최대 점수
max_score = max(scores)

# 각 점수를 최대 점수로 나누고 100을 곱한 후, 그 값을 누적하여 합산
total_normalized = 0.0
for score in scores:
    normalized_score = (score / max_score) * 100
    total_normalized += normalized_score

# 새로운 평균 계산
new_average = total_normalized / n

print(new_average)
