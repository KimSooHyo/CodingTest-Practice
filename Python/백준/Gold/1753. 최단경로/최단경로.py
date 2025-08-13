import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
dist = [INF] * (V+1)
def dijkstra(start):
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        
        if cur_dist > dist[cur_node]:
            continue
        for next, w in graph[cur_node]:
            cost = cur_dist + w
            if dist[next] > cost:
                dist[next] = cost
                heapq.heappush(heap, (cost, next))

dijkstra(K)
for i in range(1, V + 1):
    print(dist[i] if dist[i] != INF else "INF")