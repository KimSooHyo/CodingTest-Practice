from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [i for i in range(101)]

for _ in range(N):
    x, y =map(int, input().split())
    board[x] = y
    
for _ in range(M):
    u, v = map(int, input().split())
    board[u] = v
    
visited = [False] * 101
q = deque()
q.append((1,0)) #현재 위치, 주사위 횟수
visited[1] = True

while q:
    pos, cnt = q.popleft()
    if pos == 100:
        print(cnt)
        break
    
    for dice in range(1, 7):
        next = pos + dice
        
        if next <= 100 and not visited[board[next]]:
            visited[board[next]] = True
            q.append((board[next], cnt + 1))