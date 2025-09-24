import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
def dfs(current_node):
    visited[current_node] = True
    for next_node in graph[current_node]:
        if not visited[next_node]:
            dfs(next_node)

dfs(1)
print(sum(visited) - 1)