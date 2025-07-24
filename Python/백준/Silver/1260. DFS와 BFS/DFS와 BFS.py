import sys
sys.setrecursionlimit(1000000)
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1, N+1):
    graph[i].sort()
    
visited_dfs = [False] * (N+1)
def dfs(start_node):
    visited_dfs[start_node] = True
    print(start_node, end=' ')
    
    for node in graph[start_node]:
        if not visited_dfs[node]:
            dfs(node)

visited_bfs = [False] * (N+1)
def bfs(start_node):
    queue = deque([start_node])
    visited_bfs[start_node] = True
    
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for next_node in graph[node]:
            if not visited_bfs[next_node]:
                queue.append(next_node)
                visited_bfs[next_node] = True
                
dfs(V)
print()
bfs(V)