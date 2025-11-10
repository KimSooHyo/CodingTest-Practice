square = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            square[y][x] = 1
            
total = 0
for y in range(100):
    total += sum(square[y])
    
print(total)