import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1, N+1):
    graph[i].sort(reverse=True)
    
visited = [False] * (N+1)
order = [0] * (N+1)
cnt = 1

def dfs(start_node):
    global cnt
    visited[start_node] = True
    order[start_node] = cnt
    cnt += 1
    
    for node in graph[start_node]:
        if not visited[node]:
            dfs(node)
            
dfs(R)

for i in range(1, N+1):
    print(order[i])