import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
sequence = []
visited = [False] * (max(nums) +1)

def backtrack():
    if len(sequence) == M:
        print(*sequence)
        return
    
    for n in nums:
        if not visited[n]:
            sequence.append(n)
            for j in range(n+1):
                visited[j] = True
            backtrack()
            sequence.pop()
            for j in range(n+1):
                visited[j] = False
                
backtrack()