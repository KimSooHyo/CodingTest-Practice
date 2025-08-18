def solution(my_string):
    answer = 0
    now = ''
    idx = 0
    while idx < len(my_string):
        c = my_string[idx]
        
        if c.isdigit():
            now += my_string[idx]
        else:
            if now:
                answer += int(now)
                now = ''
        idx += 1
            
    if now:
        answer += int(now)
    return answer