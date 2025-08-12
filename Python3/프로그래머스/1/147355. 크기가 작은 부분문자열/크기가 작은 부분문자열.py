def solution(t, p):
    answer = 0
    nums = []
    l = len(p)
    for i in range(len(t)-l+1):
        n = t[i:i+l]
        if int(n) <= int(p):
            answer += 1
     
    return answer