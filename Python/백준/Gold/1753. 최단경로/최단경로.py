import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input().strip())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    u, dest, w = map(int, input().split())
    graph[u].append((dest, w))

inf = 99999999
distance = [inf] * (v+1)

def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]
    
    while heap:
        dist, now = heapq.heappop(heap)
        
        if distance[now] < dist:
            continue
        
        for neighbor, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
                
dijkstra(k)
for i in range(1, v + 1):
    print(distance[i] if distance[i] != inf else "INF")