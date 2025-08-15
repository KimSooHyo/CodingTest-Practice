import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
    
nums.sort()

sequence = []
visited = [False] * (max(nums)+1)
def backtrack():
    if len(sequence) == M:
        print(*sequence)
        return
        
    for n in nums:
        if not visited[n]:
            sequence.append(n)
            visited[n] = True
            backtrack()
            sequence.pop()
            visited[n] = False
        
backtrack()