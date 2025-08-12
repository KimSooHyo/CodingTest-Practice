def solution(emergency):
    answer = []
    rank = sorted(emergency, reverse=True)
    for e in emergency:
        answer.append(rank.index(e)+1)
    return answer