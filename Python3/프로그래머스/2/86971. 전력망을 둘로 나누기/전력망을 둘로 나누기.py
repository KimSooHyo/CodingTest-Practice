"""
- 최적이나 최소를 구하는 것이 아님 -> 깊이 우선 탐색
- 전체 전력망에서 전선을 하나씩 제거하며 두 전력망의 송전탑 개수 차이를 구하고 최솟값을 반환하면 됨
"""

#그래프 생성
def build_graph(n, wires):
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    return graph

#깊이 우선 탐색 함수
def dfs(node, parent, graph):
    cnt = 1
    #현재 노드의 자식 노드들에 방문
    for chile in graph[node]:
        #부모 노드가 아닌 경우에만 탐색
        if chile != parent:
            cnt += dfs(chile, node, graph)
    return cnt

def solution(n, wires):
    graph = build_graph(n ,wires)
    min_diff = float("inf")
    
    for a,b in wires:
        #간선 제거
        graph[a].remove(b)
        graph[b].remove(a)
        
        #각 전력망 송전탑 개수 계산
        cnt_a = dfs(a,b,graph)
        cnt_b = n - cnt_a
        
        #최솟값 갱신
        min_diff = min(min_diff, abs(cnt_a - cnt_b))
        
        #간선 복원
        graph[a].append(b)
        graph[b].append(a)        
        
    return min_diff