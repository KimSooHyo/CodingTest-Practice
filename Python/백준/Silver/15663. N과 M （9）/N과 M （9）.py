import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

sequence = []
visited = [False] * N

def backtrack(start):
    if len(sequence) >= M:
        print(*sequence)
        return
    
    prev = 0
    for i in range(N):
        if not visited[i] and prev != nums[i]:
            visited[i] = True
            sequence.append(nums[i])
            prev = nums[i]
            backtrack(i)
            sequence.pop()
            visited[i] = False
        
backtrack(0)