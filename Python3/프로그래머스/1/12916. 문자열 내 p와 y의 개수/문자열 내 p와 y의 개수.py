def solution(s):
    p_cnt = 0
    y_cnt = 0
    
    for c in s:
        if c == 'p' or c == 'P':
            p_cnt += 1
        elif c == 'y' or c == 'Y':
            y_cnt += 1
    
    return p_cnt == y_cnt