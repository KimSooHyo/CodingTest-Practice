import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name_to_num = {}
num_to_name = {}

for i in range(1, N+1):
    book = input().strip()
    name_to_num[book] = i
    num_to_name[i] = book
    
for _ in range(M):
    query = input().strip()
    if query.isdigit():
        print(num_to_name[int(query)])
    else:
        print(name_to_num[query])