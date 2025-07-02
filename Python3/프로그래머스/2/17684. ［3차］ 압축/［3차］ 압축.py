def solution(msg):
    answer = []
    
    dict = {}
    dict = {chr(i + 64): i for i in range(1, 27)}
    index = 27
    
    i = 0
    while i < len(msg):
        w = msg[i]
        j = i + 1

        while j <= len(msg) and msg[i:j] in dict:
            w = msg[i:j]
            j += 1
        
        answer.append(dict[w])
        
        if j <= len(msg):  # 다음 글자 c가 존재하면
            dict[msg[i:j]] = index
            index += 1
        i += len(w)
    return answer