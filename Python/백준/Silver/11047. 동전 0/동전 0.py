import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
total = 0

for _ in range(N):
    coin = int(input())
    coins.append(coin)
    
coins.sort(reverse=True)

for coin in coins:
    if K <= 0:
        break
    
    total += (K // coin)
    K %= coin
    
print(total)