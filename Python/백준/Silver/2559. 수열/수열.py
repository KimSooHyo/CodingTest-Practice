import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

# 첫 구간 합
window_sum = sum(nums[:k])
max_sum = window_sum

# 슬라이딩 윈도우
for i in range(k, n):
    window_sum += nums[i] - nums[i - k]
    if window_sum > max_sum:
        max_sum = window_sum

print(max_sum)
