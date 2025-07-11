import sys
input = sys.stdin.readline
nums = [[0] for _ in range(9)]

for i in range(9):
    nums[i] = list(map(int, input().split()))
    
max_num = -999    
max_idx = []
for i in range(9):
    if max_num < max(nums[i]):
        max_num = max(nums[i])
        max_idx = [i+1, nums[i].index(max_num) + 1]
print(max_num)
print(*max_idx)