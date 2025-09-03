def solution(s, skip, index):
    answer = ''
    
    alpha = [char for char in "abcdefghijklmnopqrstuvwxyz" if char not in skip]
    
    for c in s:
        idx = (alpha.index(c)+index) % len(alpha)
        answer += alpha[idx]
    
    return answer