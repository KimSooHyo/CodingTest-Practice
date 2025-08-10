import sys
from collections import deque
input = sys.stdin.readline

com = int(input())
n = int(input())
graph = [[] for _ in range(com+1)]
for _ in range(n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False] * (com+1)
def bfs(start):
    visited[start] = True
    cnt = 0
    
    queue = deque()
    queue.append(start)
    
    while queue:
        node = queue.popleft()
        
        for next in graph[node]:
            if graph[next] and not visited[next]:
                queue.append(next)
                visited[next] = True
                cnt += 1
                
    return cnt

print(bfs(1))