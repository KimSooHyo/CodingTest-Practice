import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]


for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
def dijkstra(start):
    dist = [INF] * (N+1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        if cur_dist > dist[cur_node]:
            continue
        for next, w in graph[cur_node]:
            cost = cur_dist + w
            if cost < dist[next]:
                dist[next] = cost
                heapq.heappush(heap, (cost, next))
    return dist
v1, v2 = map(int, input().split())
dist1 = dijkstra(1)
distv1 = dijkstra(v1)
distv2 = dijkstra(v2)

# 경로1: 1 -> v1 -> v2 -> N
path1 = dist1[v1] + distv1[v2] + distv2[N]
# 경로2: 1 -> v2 -> v1 -> N
path2 = dist1[v2] + distv2[v1] + distv1[N]

result = min(path1, path2)
print(result if result < INF else -1)