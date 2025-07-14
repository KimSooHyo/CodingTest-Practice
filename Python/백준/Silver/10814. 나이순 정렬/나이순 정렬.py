import sys
input = sys.stdin.readline

members = []
n = int(input())
for i in range(n):
    member = list(map(str, input().split()))
    member.append(i)
    members.append(member)
    
sorted_members = sorted(members, key= lambda x: (int(x[0]), x[2]))

for member in sorted_members:
    print(member[0], member[1])