t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    day = n//c
    if n%c > 0:
        day += 1
    print(day)