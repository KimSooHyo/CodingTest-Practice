N, K = map(int, input().split())
nums = list(map(int, input().split()))

max_sum = -99999999
start = 0
end = K
for i in range(N - K + 1):
    max_sum = max(max_sum, sum(nums[start + i : end + i]))
    
print(max_sum)