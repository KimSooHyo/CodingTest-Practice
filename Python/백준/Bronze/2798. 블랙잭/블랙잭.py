"""
N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.
"""
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

combi = combinations(cards, 3)

diff = 300000
result = 0
for c in combi:
    if sum(c) > M:
        continue
    elif abs(M - sum(c)) < diff:
        diff = abs(M - sum(c))
        result = sum(c)
        
print(result)