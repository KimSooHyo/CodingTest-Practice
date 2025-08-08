import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

high = low = 0
nums_sum = 0

INF = float('inf')
length = INF

while True:
    # print(nums_sum)
    if nums_sum < S:
        if high >= N:
            break
        
        nums_sum += nums[high]
        high += 1
    elif nums_sum >= S:
        length = min(length, high - low)

        nums_sum -= nums[low]
        low += 1
        
if length == INF:
    print(0)
else:
    print(length)