import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M, R = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    from_node, to_node = map(int, input().strip().split())
    graph[from_node].append(to_node)
    graph[to_node].append(from_node)
    
for i in range(1, N+1):
    graph[i].sort()

visited = [False] * (N+1)
cnt = 1
order = [0] * (N+1)

def dfs(start):
    global cnt
    visited[start] = True
    order[start] = cnt    
    cnt += 1
    for node in graph[start]:
        if visited[node] == False:
            dfs(node)
            
dfs(R)

for i in range(1, N+1):
    print(order[i])