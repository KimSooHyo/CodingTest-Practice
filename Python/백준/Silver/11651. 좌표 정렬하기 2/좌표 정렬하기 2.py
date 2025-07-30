import sys
input = sys.stdin.readline

n = int(input())
points = [[] for _ in range(n)]

for i in range(n):
    points[i] = list(map(int, input().split()))
    
sorted_points = sorted(points, key=lambda x: (x[1], x[0]))

for i in range(n):
    print(*sorted_points[i])