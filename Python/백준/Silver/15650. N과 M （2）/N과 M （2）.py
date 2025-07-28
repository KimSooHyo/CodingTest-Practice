#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False] * (N+1)
sequence = []

def backtracking(start):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(start, N+1):
        if not visited[i]:
            visited[i]=True
            sequence.append(i)
            
            backtracking(i+1)
            sequence.pop()
            visited[i]=False
            
backtracking(1)