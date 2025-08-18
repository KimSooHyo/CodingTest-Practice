def solution(k, score):
    legend = []
    answer = []
    for s in score:
        legend.append(s)
        legend.sort(reverse=True)
        if len(legend) > k:
            legend.pop()
        answer.append(legend[-1])
       
    return answer