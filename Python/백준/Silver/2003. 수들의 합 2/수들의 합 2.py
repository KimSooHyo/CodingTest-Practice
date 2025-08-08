import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

start = end = 0
sum_A = 0
ans = 0

while True:
    if M <= sum_A:
        sum_A -= A[start]
        start += 1
    else:
        if end >= N:
            break
            
        sum_A += A[end]
        end += 1
    
    if sum_A == M:
        ans += 1
        
print(ans)