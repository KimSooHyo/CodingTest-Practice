n, k = map(int, input().split())
num_list = []

for i in range(1, n+1):
    if n % i == 0:
        num_list.append(i)

# sorted_list = sorted(num_list, reverse=True)
if k > len(num_list):
    print(0)
else:
    print(num_list[k-1])