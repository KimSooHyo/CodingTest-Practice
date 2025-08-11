from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def bfs(start):
    queue = deque()
    visited[start] = False
    queue.append(start)
    
    while queue:
        node = queue.popleft()
        
        for next in graph[node]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        cnt += 1
    
print(cnt)