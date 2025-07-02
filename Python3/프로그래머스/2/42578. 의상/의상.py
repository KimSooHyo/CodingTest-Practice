from collections import Counter
from itertools import combinations
import itertools

def solution(clothes):
    dict = {}
    
    for cloth in clothes:
        name, kind = cloth[0], cloth[1]

        if kind not in dict:
            dict[kind] = []
        dict[kind].append(name)
    
    # 경우의 수 계산
    total = 1
    for items in dict.values():
        total *= (len(items) + 1)  # 입지 않는 경우 포함

    return total - 1  # 전부 안 입는 경우 빼기