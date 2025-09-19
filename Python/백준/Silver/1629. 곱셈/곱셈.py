a, b, c = map(int, input().split())

def solution(a, b, c):
    if b == 1:
        return a % c
    
    half = solution(a, b // 2, c)
    
    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c
    
print(solution(a,b,c))