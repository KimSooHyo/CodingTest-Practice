def solution(s):
    answer = ''
    words = s.split(' ')
    for w in words:
        for i, c in enumerate(w):
            if i % 2 == 0:
                answer += (c.upper())
            else:
                answer += (c.lower())
        answer += (' ')
    return answer[:-1]