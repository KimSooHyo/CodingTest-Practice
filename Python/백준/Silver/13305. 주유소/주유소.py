import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
total = 0

for i in range(n-1):
    if price[i] < min_price:
        min_price = price[i]
    total += road[i] * min_price
    
print(total)