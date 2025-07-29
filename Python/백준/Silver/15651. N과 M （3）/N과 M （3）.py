import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# visitied = [False] * (N+1)
sentence = []

def backtrack():

    if len(sentence) == M:
        print(*sentence)
        return

    for i in range(1, N+1):
        sentence.append(i)
        backtrack()
        sentence.pop()
        
backtrack()