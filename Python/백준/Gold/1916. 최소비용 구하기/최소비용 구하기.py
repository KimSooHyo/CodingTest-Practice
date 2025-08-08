import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
start, end = map(int, input().split())

def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]
    
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        
        for neighbor, cost in graph[now]:
            new_cost = cost + dist
            if new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
                
dijkstra(start)
print(distance[end])