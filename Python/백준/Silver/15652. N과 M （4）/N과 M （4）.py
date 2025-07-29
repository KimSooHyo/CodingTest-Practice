import sys
input = sys.stdin.readline

N, M = map(int, input().split())

sequence = []

def backtrack(start):
    if len(sequence) == M:
        print(*sequence)
        return
    
    for i in range(start, N+1):
        sequence.append(i)
        backtrack(i)
        sequence.pop()
        
backtrack(1)