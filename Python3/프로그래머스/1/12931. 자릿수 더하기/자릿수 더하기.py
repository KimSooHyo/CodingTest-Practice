def solution(n):
    sum = 0
    while True:
        if n <= 9:
            sum += n
            break
        sum += n%10
        n //= 10

    return sum