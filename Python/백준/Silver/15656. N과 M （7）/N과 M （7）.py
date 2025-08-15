import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
sequence = []
def backtrack():
    if len(sequence) == M:
        print(*sequence)
        return
    
    for n in nums:
        sequence.append(n)
        backtrack()
        sequence.pop()
        
backtrack()