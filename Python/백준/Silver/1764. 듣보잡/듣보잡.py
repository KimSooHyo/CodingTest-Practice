import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name_dic = {}

for _ in range(N+M):
    name = input().strip()
    if name in name_dic:
        name_dic[name] += 1
    else:
        name_dic[name] = 1
        
result = sorted([name for name, count in name_dic.items() if count == 2])

print(len(result))
for name in result:
    print(name)