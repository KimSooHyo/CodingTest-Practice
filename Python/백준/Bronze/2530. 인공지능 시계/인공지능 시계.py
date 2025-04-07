h, m, s = map(int, input().split())
n = int(input())

total_sec = h * 3600 + m * 60 + s + n

h = (total_sec//3600)%24
m = (total_sec%3600)//60
s = total_sec%60

print(h,m,s)