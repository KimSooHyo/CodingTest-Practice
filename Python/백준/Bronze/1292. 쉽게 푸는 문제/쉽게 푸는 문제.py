nums = []
for i in range(300):
    for j in range(i):
        nums.append(i)
        
a, b = map(int, input().split())

ans_nums = nums[(a-1):b]

print(sum(ans_nums))