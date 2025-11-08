num = list(input().strip())
for i in range(len(num)-1, 0, -1):
    n = int(num[i])
    if n >= 5:
        num[i-1] = str(int(num[i-1]) + 1)
    num[i] = '0'
    
print(int("".join(num)))