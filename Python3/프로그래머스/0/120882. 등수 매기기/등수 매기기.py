def solution(score):
    min_score = []
    for s in score:
        min_score.append(sum(s)/2)
    answer = []
    for a in min_score:
        rank = 1
        for b in min_score:
            if b > a:
                rank += 1
        answer.append(rank)
    
    return answer