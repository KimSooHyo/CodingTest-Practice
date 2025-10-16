from collections import deque

# 입력 받기
N, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#회전 함수
def rotate(grid, L):
    n = 2 ** L 
    size = len(grid)
    new_grid = [[0] * size for _ in range(size)]

    #부분 단위로 회전 수행
    for y in range(0, size, n):
        for x in range(0, size, n):
            for i in range(n):
                for j in range(n):
                    new_grid[y + j][x + n - 1 - i] = grid[y + i][x + j]
    return new_grid

#얼음 녹이기 함수
def ice(grid):
    size = len(grid)
    melt_list = [] #녹일 칸들의 좌표 저장

    for y in range(size):
        for x in range(size):
            if grid[y][x] == 0:
                continue

            cnt = 0 #주변 얼음 칸 개수
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < size and 0 <= nx < size and grid[ny][nx] > 0:
                    cnt += 1

            if cnt < 3:
                melt_list.append((y, x))

    # 얼음 녹이기
    for y, x in melt_list:
        grid[y][x] -= 1

    return grid

# 가장 큰 얼음 덩어리 찾기 (BFS)
def biggest_ice(grid):
    size = len(grid)
    visited = [[False] * size for _ in range(size)]
    max_chunk = 0

    for y in range(size):
        for x in range(size):
            #새로운 얼음 덩어리 발견 시 BFS 시작
            if grid[y][x] > 0 and not visited[y][x]:
                queue = deque([(y, x)])
                visited[y][x] = True
                cnt = 1 # 현재 덩어리 크기

                while queue:
                    cy, cx = queue.popleft()
                    for i in range(4):
                        ny, nx = cy + dy[i], cx + dx[i]
                        if 0 <= ny < size and 0 <= nx < size:
                            if not visited[ny][nx] and grid[ny][nx] > 0:
                                visited[ny][nx] = True
                                queue.append((ny, nx))
                                cnt += 1

                max_chunk = max(max_chunk, cnt)

    return max_chunk

# 회전 + 얼음 녹이기
for l in L:
    grid = rotate(grid, l)
    grid = ice(grid)

#결과 계산 및 출력
total_ice = sum(map(sum, grid))
max_chunk_size = biggest_ice(grid)

print(total_ice)
print(max_chunk_size)
