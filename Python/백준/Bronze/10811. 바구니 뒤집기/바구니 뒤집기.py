"""
5 4
1 2
3 4
1 4
2 2

1 2 3 4 5
2 1 3 4 5
2 1 4 3 5
3 4 1 2 5
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(1,n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    for k in range((j-i+1)//2):
        nums[i+k], nums[j-k] = nums[j-k], nums[i+k]
        
print(" ".join(map(str, nums)))