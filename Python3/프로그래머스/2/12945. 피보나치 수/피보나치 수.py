def solution(n):
    answer = 0
    nums = [0] * (n+1)
    nums[1] = 1
    for i in range(2, n):
        nums[i] = nums[i-2] + nums[i-1]
        
    answer = nums[n-1] + nums[n-2]
    return answer%1234567