#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False] * (N+1)
sequence = []

def backtracking():
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i]=True
            sequence.append(i)
            backtracking()
            sequence.pop()
            visited[i]=False
            
backtracking()