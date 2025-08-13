def solution(d, budget):
    answer = 0
    remain = budget
    d.sort()
    
    for c in d:
        if c <= remain:
            answer += 1
            remain -= c
        else:
            break
    return answer