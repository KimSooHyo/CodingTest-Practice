import sys
input = sys.stdin.readline

x, y = map(int, input().split())
n = int(input().strip())

garo = []
sero = []
for i in range(n):
    dir, num = map(int, input().split())
    if dir == 0:
        garo.append(num)
    else:
        sero.append(num)

garo.append(y)
sero.append(x)
garo.sort()
sero.sort()

extend = []

for i in range(len(garo) -1 , 0, -1):
    if i > 0:
        garo[i] -= garo[i-1]
for i in range(len(sero) -1 , 0, -1):
    if i > 0:
        sero[i] -= sero[i-1]

for g in garo:
    for s in sero:
        extend.append(g*s)
        
print(max(extend))