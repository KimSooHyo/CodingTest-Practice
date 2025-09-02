def solution(name, yearning, photo):
    answer = []
    
    for ph in photo:
        cnt = 0
        
        for p in ph:
            if p in name:
                idx = name.index(p)
                cnt += yearning[idx]
        answer.append(cnt)
    return answer