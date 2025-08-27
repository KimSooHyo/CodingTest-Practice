N, M = map(int, input().split())
visited = [False] * (M)

cnt = 0
for _ in range(N):
    line = input()
    
    for i, l in enumerate(line):
        if l == 'X':
            visited[i] = True
    
    if 'X' not in line:
        cnt += 1


print(max(cnt, visited.count(False)))