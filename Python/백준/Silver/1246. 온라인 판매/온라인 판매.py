n, m = map(int, input().split())

prices = list(int(input()) for _ in range(m))
prices.sort()
max_price = 0
answer = 0

for i, p in enumerate(prices):
    total_price = p * min(m-i, n)
    if total_price > max_price:
        max_price = total_price
        answer = p
    
print(answer, max_price)