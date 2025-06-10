"""
    1 1 2 6 24
    120 720 49nn
    
    """
nums = [0] * 25
nums[0] = 1
for i in range(1, 25):
    nums[i] = nums[i-1] * i 
    
#입력
n = int(input())
sum = n
for i in range(24, -1, -1):
    if sum >= nums[i]:
        sum -= nums[i]
    
if n != 0 and sum == 0:
    print("YES")
else:
    print("NO")