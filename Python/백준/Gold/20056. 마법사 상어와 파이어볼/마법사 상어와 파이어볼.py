import sys
input = sys.stdin.readline

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())

fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])
    
def move_fireballs(fireballs):
    grid = [[[] for _ in range(N)] for _ in range(N)]
    for r, c, m, s, d in fireballs:
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        grid[nr][nc].append([m, s, d])
    return grid

def merge_and_split(grid):
    new_fireballs = []
    for r in range(N):
        for c in range(N):
            if len(grid[r][c]) == 0:
                continue
            if len(grid[r][c]) == 1:
                m, s, d = grid[r][c][0]
                new_fireballs.append([r, c, m, s, d])
            else:
                total_m, total_s = 0, 0
                cnt = len(grid[r][c])
                is_even, is_odd = True, True
                for m, s, d in grid[r][c]:
                    total_m += m
                    total_s += s
                    if d % 2 == 0:
                        is_odd = False
                    else:
                        is_even = False
                
                new_m = total_m // 5
                if new_m == 0:
                    continue
                new_s = total_s // cnt
                if is_even or is_odd:
                    dirs = [0,2,4,6]
                else:
                    dirs = [1,3,5,7]
                for nd in dirs:
                    new_fireballs.append([r,c,new_m,new_s, nd])
    return new_fireballs

for _ in range(K):
    grid = move_fireballs(fireballs)
    fireballs = merge_and_split(grid)
    
print(sum(m for r, c, m, s, d in fireballs))