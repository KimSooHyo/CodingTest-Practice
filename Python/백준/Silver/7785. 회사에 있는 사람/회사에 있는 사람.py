import sys
input = sys.stdin.readline

n = int(input())
name_set = set()
for i in range(n):
    name, log = input().strip().split()
    if log == 'enter':
        name_set.add(name)
    else:
        if name in name_set:
            name_set.remove(name)
        
sorted_set = sorted(name_set, reverse=True)

for name in sorted_set:
    print(name)