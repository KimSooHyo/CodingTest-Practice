import sys
from collections import Counter
input = sys.stdin.readline

N, M = map(int, input().split())

words = []
for _ in range(N):
    w = input().strip()
    if len(w) >= M:
        words.append(w)
        
cnt = Counter(words)

answer_list = []
for w in cnt.keys():
    answer_list.append((w, cnt[w] , len(w)))
    
sorted_list = sorted(answer_list, key=lambda x: (-x[1], -x[2], x[0]))

for i in range(len(sorted_list)):
    print(sorted_list[i][0])