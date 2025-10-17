n = int(input())

num_list = []
for _ in range(n):
    a, b = map(int, input().split())
    num_list.append(b-a)
    
num_list.sort()
# print("num_list :", num_list)
if n % 2 == 1:
    print(1)
else:
    n1 = num_list[n//2 - 1]
    n2 = num_list[n//2]
    print(n2 - n1 + 1)