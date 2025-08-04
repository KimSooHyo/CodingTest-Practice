import sys
input = sys.stdin.readline

n = int(input())
times = 0
names = set()
for _ in range(n):
    query = input().strip()
    if query == "ENTER":
        times += len(names)
        names = set()
    else:
        names.add(query)

times += len(names)      
print(times)