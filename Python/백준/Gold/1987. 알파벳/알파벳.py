from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

r, c = map(int, input().split())
grid = [[] for _ in range(r)]

for i in range(r):
    grid[i] = list(input().strip())

cx = [1,-1,0,0]
cy = [0,0,1,-1]
alpha = [False] * 26
answer = 0
visited = set()

def dfs(y, x, cnt):
    global answer
    answer = max(answer, cnt)
    state = (y, x, tuple(alpha))
    if state in visited:
        return
    visited.add(state)
    for i in range(4):
        nx = x + cx[i]
        ny = y + cy[i]
        
        if 0 <= nx < c and 0 <= ny < r:
            idx = ord(grid[ny][nx]) - ord('A')
            if alpha[idx] == False:
                alpha[idx] = True
                dfs(ny, nx, cnt+1)
                alpha[idx] = False
    
alpha[ord(grid[0][0]) - ord('A')] = True
dfs(0,0,1)

print(answer)