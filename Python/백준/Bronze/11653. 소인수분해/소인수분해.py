n = int(input())
cnt = 2
while n > 1:
    if cnt > n:
        break
    
    if n % cnt == 0:
        n //= cnt
        print(cnt)
    else:
        cnt += 1