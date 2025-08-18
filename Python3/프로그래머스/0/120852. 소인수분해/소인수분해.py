def solution(n):
    answer = set()
    num = 2
    
    if n == 2:
        return [2]
    
    while num * num <= n:
        if n % num == 0:
            n //= num
            answer.add(num)
        else:
            num += 1
    if n > 1:  # 마지막 남은 소수
        answer.add(n)
        
    return sorted(answer)