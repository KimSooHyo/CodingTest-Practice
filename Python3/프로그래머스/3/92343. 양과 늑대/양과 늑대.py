def solution(info, edges):
    answer = 0
    graph = [[] for _ in range(len(info))]
    for e in edges: #트리 저장, 부모->자식 관계만 저장
        u, v = e
        graph[u].append(v)
    
    #탐색
    def dfs(sheep, wolf, next_nodes):
        nonlocal answer
        answer = max(answer, sheep) #최대 양 개수 저장

        for node in next_nodes:
            new_sheep = sheep + (1 if info[node] == 0 else 0) #양 수 업데이트
            new_wolf = wolf + (1 if info[node] == 1 else 0) #늑대 수 업데이트
            
            if new_sheep > new_wolf: #양이 더 많은 경우에만
                new_next_nodes = next_nodes[:]
                new_next_nodes.remove(node)
                new_next_nodes.extend(graph[node]) #다음으로 갈 수 있는 노드 업데이트
                dfs(new_sheep, new_wolf, new_next_nodes)
            
    dfs(1,0,graph[0])
    
    return answer