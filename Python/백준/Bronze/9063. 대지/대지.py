import sys
input = sys.stdin.readline

N = int(input())

garo = []
sero = []
for _ in range(N):
    g, s = map(int, input().strip().split())
    garo.append(g)
    sero.append(s)
    
amount = (max(garo) - min(garo)) * (max(sero) - min(sero))
print(amount)