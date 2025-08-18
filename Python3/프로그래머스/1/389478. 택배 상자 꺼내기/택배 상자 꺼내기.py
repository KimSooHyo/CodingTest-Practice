def solution(n, w, target):
    
    h = (n + w - 1) // w  # 올림 나눗셈
    box = [[0]*w for _ in range(h)]
    
    num = 1
    for row in range(h):
        if row % 2 == 0:  # 왼→오
            for col in range(w):
                if num <= n:
                    box[row][col] = num
                    num += 1
        else:  # 오→왼
            for col in range(w-1, -1, -1):
                if num <= n:
                    box[row][col] = num
                    num += 1

    # target 위치 찾기
    t_row, t_col = -1, -1
    for i in range(h):
        for j in range(w):
            if box[i][j] == target:
                t_row, t_col = i, j
                break
    
    # 같은 열 위쪽에 있는 상자 개수 + 자기 자신
    count = 0
    for r in range(t_row, h):
        if box[r][t_col] != 0:
            count += 1
    return count