import sys
from collections import deque
input = sys.stdin.readline

computer = int(input())
n = int(input())

graph = [[] for _ in range(computer+1)]
for i in range(n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [0] * (computer+1)

def dfs(start_node):
    global cnt
    visited[start_node] = 1
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                queue.append(next_node)
                
         
dfs(1)       
print(sum(visited)-1)