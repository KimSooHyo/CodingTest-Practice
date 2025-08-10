import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0

def dfs(idx, current_sum):
    global cnt
    if idx == N:
        return 
    
    new_sum = current_sum + nums[idx]
    
    if new_sum == S:
        cnt += 1
    
    dfs(idx+1, new_sum)
    dfs(idx+1, current_sum)
    
dfs(0,0)
print(cnt)