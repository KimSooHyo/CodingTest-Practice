import sys
input = sys.stdin.readline

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]

sorted_time = sorted(time, key=lambda x: (x[1], x[0]))

cnt = 0
start_time = 0
for t in sorted_time:
    if start_time <= t[0]:
        cnt += 1
        start_time = t[1]
        
print(cnt)