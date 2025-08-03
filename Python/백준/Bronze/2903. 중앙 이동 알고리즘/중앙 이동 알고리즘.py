n = int(input())

points = []
j = 2
for _ in range(2, 20):
    points.append((j**2))
    j = (j * 2)-1
    
print(points[n])