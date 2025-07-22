import sys
from collections import deque
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1, N+1):
    graph[i].sort(reverse=True)
    
visited = [False] * (N+1)
order = [0] * (N+1)
cnt = 1

def bfs(start_node):
    global cnt
    queue = deque([start_node])
    visited[start_node] = True
    
    while queue:
        node = queue.popleft()
        order[node] = cnt
        cnt += 1
        
        for nex_node in graph[node]:
            if not visited[nex_node]:
                visited[nex_node] = True
                queue.append(nex_node)
                
bfs(R)
for i in range(1, N+1):
    print(order[i])