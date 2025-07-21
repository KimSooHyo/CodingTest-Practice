import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1, N+1):
    graph[i].sort()
    
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
        
        for next_node in graph[node]:
            if visited[next_node] == False:
                queue.append(next_node)
                visited[next_node] = True
                
bfs(R)

for i in range(1, N+1):
    print(order[i])