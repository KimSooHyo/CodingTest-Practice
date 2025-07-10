import sys
sys.setrecursionlimit(10**6)

n = int(input())
nodes = [[] for _ in range(n+1)]


for _ in range(n-1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
    
parent = [0] * (n+1)
visited = [False] * (n+1)

def dfs(node):
    visited[node] = True
    for neighbor in nodes[node]:
        if not visited[neighbor]:
            parent[neighbor] = node
            dfs(neighbor)

dfs(1)

for i in range(2, n+1):
    print(parent[i])