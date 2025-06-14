n = int(input()) #26
num = n

first = n//10 # 2
second = n%10 # 6
plus = first+second # 8

cnt = 0
while(True):
    cnt += 1
    first = num//10 # 2
    second = num%10 # 6
    plus = (first+second)%10 # 8
    num = second * 10 + plus
    if (num) == n:
        break
print(cnt)