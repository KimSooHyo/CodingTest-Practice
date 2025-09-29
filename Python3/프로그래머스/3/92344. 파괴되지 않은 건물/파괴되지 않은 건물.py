def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    
    #변화량 기록
    changes = [[0] * (M+1) for _ in range(N+1)]
    
    for t, r1, c1, r2, c2, degree in skill:
        d = degree if t == 2 else -degree
        
        changes[r1][c1] += d
        changes[r1][c2+1] -= d
        changes[r2+1][c1] -= d
        changes[r2+1][c2+1] += d
        
    #누적합
    for i in range(N):
        for j in range(M):
            changes[i][j+1] += changes[i][j]
    for j in range(M):
        for i in range(N):
            changes[i+1][j] += changes[i][j]
            
    #최종 결과 계산
    for i in range(N):
        for j in range(M):
            if board[i][j] + changes[i][j] > 0:
                answer += 1
    return answer