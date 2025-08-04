import sys
input = sys.stdin.readline

names = set(["ChongChong"])
n = int(input())

for _ in range(n):
    a, b = input().strip().split()
    if a in names:
        names.add(b)
    elif b in names:
        names.add(a)
        
print(len(names))