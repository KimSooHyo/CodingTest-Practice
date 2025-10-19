import sys
input = sys.stdin.readline

N, T = map(int, input().split())
BusTime = []
for _ in range(N):
    S, I, C = map(int, input().split())
    for i in range(C):
        time = S + (I * i)
        if time >= T:
            BusTime.append(time)
            
        # print(time, BusTime)
        
if not BusTime:
    print(-1)
else:
    BusTime.sort()
    print(BusTime[0] - T)