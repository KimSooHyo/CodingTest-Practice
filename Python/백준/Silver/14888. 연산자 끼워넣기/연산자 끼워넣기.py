import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input().strip())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_val = -1_000_000_000
min_val = 1_000_000_000

def dfs(idx, current, plus, minus, mul, div):
    global max_val, min_val
    if idx == N:
        max_val = max(max_val, current)
        min_val = min(min_val, current)
        return
    num = nums[idx]
        
    if plus > 0:
        dfs(idx+1, current + num, plus-1, minus, mul, div)
    if minus > 0:
        dfs(idx+1, current - num, plus, minus-1, mul, div)
    if mul > 0:
        dfs(idx+1, current * num, plus, minus, mul-1, div)
    if div > 0:
        # C++14 기준 나눗셈
        if current < 0:
            dfs(idx + 1, -(-current // num), plus, minus, mul, div - 1)
        else:
            dfs(idx + 1, current // num, plus, minus, mul, div - 1)
        
dfs(1, nums[0], plus,  minus, mul, div)

print(max_val)
print(min_val)