def solution(n):
    answer = []
    while True:
        if n <= 0:
            break
        answer.append(n%10)
        n //= 10
    return answer