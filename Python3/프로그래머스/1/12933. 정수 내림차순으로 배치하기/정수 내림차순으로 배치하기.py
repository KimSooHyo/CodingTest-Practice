def solution(n):
    list = []
    n = str(n)
    for c in n:
        list.append(c)
    list = sorted(list, reverse=True)
    
    sum = 0
    for c in list:
        sum = sum*10 + int(c) 
    
    return sum