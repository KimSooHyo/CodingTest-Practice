from itertools import combinations_with_replacement

def score_cal(info, combi):
    score_a = score_l = 0
    for i in range(11):
        if info[i] < combi.count(10-i):
            score_l += 10-i
        elif info[i] > 0:
            score_a += 10-i
    
    return score_l - score_a

def solution(n, info):
    answer = []
    max_combi = []
    max_diff = 0
    for combi in combinations_with_replacement(range(11), n):
        diff = score_cal(info, combi)
        if max_diff < diff:
            max_diff = diff
            max_combi = list(combi)
            
    if max_diff <= 0:
        return [-1]
    else:
        for i in range(11):
            answer.append(max_combi.count(10-i))
        return answer