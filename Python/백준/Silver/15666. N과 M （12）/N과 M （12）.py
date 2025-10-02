import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

sequence = []
def backtrack(start):
    if len(sequence) >= M:
        print(*sequence)
        return
    
    prev = 0
    for i in range(start, N):
        if nums[i] == prev:
            continue
        sequence.append(nums[i])
        prev = nums[i]
        backtrack(i)
        sequence.pop()
        
backtrack(0)