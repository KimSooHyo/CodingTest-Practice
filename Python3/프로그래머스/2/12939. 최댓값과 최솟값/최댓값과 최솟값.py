def solution(s):
    char = s.split()
    num = [int(c) for c in char]
    
    answer = str(min(num)) + ' ' + str(max(num))
    
    return answer
