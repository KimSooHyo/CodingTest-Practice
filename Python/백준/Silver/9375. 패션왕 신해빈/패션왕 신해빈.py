from itertools import product
import sys
input = sys.stdin.readline

clothes = {}

t = int(input())
for i in range(t):
    n = int(input())
    clothes = {}
    
    for j in range(n):
        item, category = input().split()
        clothes.setdefault(category, []).append(item)
    
    # print(clothes)
    total = 1
    for c in clothes.values():
        total *= (len(c) + 1)

    print(total-1)