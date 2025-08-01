import sys
input = sys.stdin.readline

n = int(input())
people = []
for _ in range(n):
    x, y = map(int, input().split())
    people.append([x,y])

count = [1] * n
for i in range(n):
    for j in range(n):
        if i == j :
            continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            count[i] += 1
            
print(*count)