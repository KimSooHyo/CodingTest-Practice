import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

visitor_sum = sum(visitors[:X])
max_sum = visitor_sum
max_cnt = 1
for i in range(X, N):
    visitor_sum += visitors[i]
    visitor_sum -= visitors[i-X]
    
    if visitor_sum == max_sum:
        max_cnt += 1
    elif max_sum < visitor_sum:
        max_sum = visitor_sum
        max_cnt = 1
        
if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(max_cnt)