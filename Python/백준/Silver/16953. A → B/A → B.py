a, b = map(int, input().split())
cnt = 1

while a != b:
    if a > b:
        cnt = -1
        break
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    else:
        cnt = -1
        break
    cnt += 1
    
print(cnt)