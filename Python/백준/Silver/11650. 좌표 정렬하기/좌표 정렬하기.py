import sys
input = sys.stdin.readline

point_list = []
N = int(input())
for i in range(N):
    point = list(map(int, input().split()))
    point_list.append(point)
    
sorted_list = sorted(point_list, key = lambda x: (x[0], x[1]))

for s in sorted_list:
    print(s[0], s[1])