def solution(s):
    answer = ''
    text = set()
    
    for c in s:
        if s.count(c) == 1:
            text.add(c)
            
    return ''.join(sorted(text))