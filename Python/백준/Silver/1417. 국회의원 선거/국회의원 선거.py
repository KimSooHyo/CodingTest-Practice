n = int(input())
nums = [int(input().strip()) for _ in range(n)]

cnt = 0
while True:
    max_num = max(nums)
    max_idx = nums.index(max(nums))
    if max_idx == 0:
        if nums.count(max_num) > 1:
            cnt += 1
        break
    cnt += 1
    nums[0] += 1
    nums[max_idx] -= 1
    
print(cnt)
    