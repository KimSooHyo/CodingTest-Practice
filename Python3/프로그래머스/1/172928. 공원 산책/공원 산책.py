def solution(park, routes):
    # 시작 위치 찾기
    for i, row in enumerate(park):
        for j, value in enumerate(row):
            if value == 'S':
                x, y = i, j

    # 방향 정의
    direction = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }

    H, W = len(park), len(park[0])

    for r in routes:
        d, n = r.split()
        dx, dy = direction[d]
        n = int(n)

        nx, ny = x, y
        success = True

        # 명령 수행 전 경로 검증
        for _ in range(n):
            nx += dx
            ny += dy
            if not (0 <= nx < H and 0 <= ny < W):
                success = False
                break
            if park[nx][ny] == 'X':
                success = False
                break

        # 유효한 경우만 이동
        if success:
            x, y = nx, ny

    return [x, y]
