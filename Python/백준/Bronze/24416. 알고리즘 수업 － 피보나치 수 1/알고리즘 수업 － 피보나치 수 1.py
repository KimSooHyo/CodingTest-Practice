def fib_count(n):
    fib = [0] * (n + 1)
    fib[1] = fib[2] = 1
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]  # 이게 곧 코드1의 실행 횟수

n = int(input())
print(fib_count(n), n - 2)  # 코드1 실행 횟수, 코드2 실행 횟수
