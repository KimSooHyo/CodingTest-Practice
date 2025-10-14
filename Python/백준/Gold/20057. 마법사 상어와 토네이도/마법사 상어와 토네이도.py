import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)] #격자 입력 받음
# print(grid)

dr = [0,1,0,-1]
dc = [-1,0,1,0]

length = 1
r, c = N//2, N//2
direction = 0
path = [(r, c, direction)]

#토네이도 이동 방향 저장
while True:
    for _ in range(2):
        for _ in range(length):
            r += dr[direction]
            c += dc[direction]
            path.append((r,c,direction))
            if r == 0 and c == 0:
                break
        direction = (direction + 1) % 4
        if r == 0 and c == 0:
            break
    length += 1
    if r == 0 and c == 0:
        break
    
#한 칸 씩 이동 하면서 흩날리는 모래 업데이트
left = [
    (-1, 1, 0.01), (1, 1, 0.01),
    (-1, 0, 0.07), (1, 0, 0.07),
    (-2, 0, 0.02), (2, 0, 0.02),
    (-1, -1, 0.1), (1, -1, 0.1),
    (0, -2, 0.05)
]

right = [
    (-1, -1, 0.01), (1, -1, 0.01),
    (-1, 0, 0.07), (1, 0, 0.07),
    (-2, 0, 0.02), (2, 0, 0.02),
    (-1, 1, 0.1), (1, 1, 0.1),
    (0, 2, 0.05)
]

up = [
    (1, -1, 0.01), (1, 1, 0.01),
    (0, -1, 0.07), (0, 1, 0.07),
    (0, -2, 0.02), (0, 2, 0.02),
    (-1, -1, 0.10), (-1, 1, 0.10),
    (-2, 0, 0.05)
]
down = [
    (-1, -1, 0.01), (-1, 1, 0.01),
    (0, -1, 0.07), (0, 1, 0.07),
    (0, -2, 0.02), (0, 2, 0.02),
    (1, -1, 0.10), (1, 1, 0.10),
    (2, 0, 0.05)
]
pattern = [left,down,right,up]

out_sand = 0
# 격자 밖으로 나간 모래는 따로 계산
for r, c, direction in path[1:]:
    sand = grid[r][c]
    if sand == 0:
        continue

    grid[r][c] = 0
    spread_total = 0
    
    for dr_s, dc_s, ratio in pattern[direction]:
        nr, nc = r + dr_s, c + dc_s
        moved = int(sand * ratio)
        spread_total += moved
        
        if 0 <= nr < N and 0 <= nc < N:
            grid[nr][nc] += moved
        else:
            out_sand += moved
    
    #alpha
    alpha_r = r + dr[direction]
    alpha_c = c + dc[direction]
    remain = sand - spread_total
    if 0 <= alpha_r < N and 0 <= alpha_c < N:
        grid[alpha_r][alpha_c] += remain
    else:
        out_sand += remain

print(out_sand)