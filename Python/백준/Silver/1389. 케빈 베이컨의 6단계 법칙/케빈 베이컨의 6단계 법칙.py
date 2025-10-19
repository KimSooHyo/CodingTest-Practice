import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
def bfs(start):
    distance = [-1] * (N + 1)
    queue = deque()
    queue.append(start)
    distance[start] = distance[0] = 0
    while queue:
        node = queue.popleft()
        
        for next in graph[node]:
            if distance[next] == -1:
                queue.append(next)
                distance[next] = distance[node] + 1
    
    return sum(distance)

answer = []
for i in range(1, N+1):
    answer.append(bfs(i))
    
print(answer.index(min(answer)) + 1)