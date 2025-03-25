from collections import Counter
n = list(map(int, input().split()))

cnt = Counter(n)
cost = 0

max_cnt = max(cnt.values())
max_value = max(cnt, key=cnt.get)

if max_cnt == 3:
    cost = 10000 + max_value * 1000
elif max_cnt == 2:
    cost = 1000 + max_value * 100
else:
    cost = max(n) * 100
    
print(cost)