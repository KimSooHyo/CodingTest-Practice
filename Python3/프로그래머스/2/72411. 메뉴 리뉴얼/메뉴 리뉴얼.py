from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    
    for c in course: #각 코스 요리 길이에 대해
        menu = []
        
        for order in orders:
            comb = combinations(sorted(order), c)
            menu += comb
        
        counter = Counter(menu)
        if len(counter) != 0 and max(counter.values()) != 1:
            for m, cnt in counter.items():
                if cnt == max(counter.values()):
                    answer.append("".join(m))
                    
    return sorted(answer)