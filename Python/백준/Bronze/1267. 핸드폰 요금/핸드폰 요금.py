import sys

num = int(sys.stdin.readline().strip())

time = list(map(int, input().split()))
Y = 0
M = 0

for i in range(len(time)):
    Y = Y + (time[i]//30 + 1) * 10
    M = M + (time[i]//60 + 1) * 15

if Y < M:
    print("Y", Y)
elif M < Y:
    print("M", M)
else:
    print("Y M", Y)