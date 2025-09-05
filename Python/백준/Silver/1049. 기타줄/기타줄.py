import sys
input = sys.stdin.readline

N, M = map(int, input().split())

set_price = []
one_price = []

for _ in range(M):
    set, one = map(int, input().split())
    set_price.append(set)
    set_price.append(one*6)
    one_price.append(one)
    
answer = 0
min_set = min(set_price)
min_one = min(one_price)
while N > 0:
    if N >= 6:
        N -= 6
        answer += min_set
    else:
        if min_one*N > min_set:
            N -= 6
            answer += min_set
        else:
            N -= 1
            answer += min_one
        
print(answer)