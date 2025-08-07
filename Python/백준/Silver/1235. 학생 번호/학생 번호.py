import sys
input = sys.stdin.readline

n = int(input().strip())
names = list(str(input().strip()) for _ in range(n))
min_k = len(names[0])

for i in range(len(names[0])):
    new_names = set()
    for name in names:
        new_names.add(name[i:])
    if len(new_names) == len(names):
        min_k = len(names[0]) - i

# print(new_names)
print(min_k)