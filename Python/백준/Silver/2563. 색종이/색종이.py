n = int(input())
total = [[0] * 100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    
    for i in range(x, x+10):
        for j in range(y, y+10):
            total[i][j] = 1

sum = 0
for t in total:
    sum += t.count(1)
    
print(sum)
