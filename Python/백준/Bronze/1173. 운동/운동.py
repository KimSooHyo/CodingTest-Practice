"""
1. 초기 맥박은 m, N분 운동해야함
2. 운동하면 +T, 휴식하면 -R
3. 맥박은 m보다 크거나 같고 M보다 작거나 같아야함
"""
N, m, M, T, R = map(int, input().split())

pulse = m
time = 0
cnt = 0
while(cnt < N):
    
    if m + T > M:
        break

    if (pulse+T) <= M:
        cnt += 1
        pulse += T
    else:
        pulse -= R
        if pulse < m:
            pulse = m
        
    time += 1
    
if cnt == N:
    print(time)
else:
    print('-1')