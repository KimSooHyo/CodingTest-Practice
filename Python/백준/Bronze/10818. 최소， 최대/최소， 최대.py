num = int(input())

min = 1000000
max = -1000000

arr = list(map(int, input().split()))

for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i

print(min)       
print(max)
