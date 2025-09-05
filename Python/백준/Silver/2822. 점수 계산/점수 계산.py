import sys
input = sys.stdin.readline

scores = []

for i in range(1, 9):
    s = int(input())
    scores.append([i, s])
    
sorted_scores = sorted(scores, key=lambda x:x[1], reverse=True)

sliced_scores = sorted_scores[:5]

total = 0
for c in sliced_scores:
    total += c[1]
print(total)

sorted_sliced = sorted(sliced_scores, key= lambda x: x[0])

for c in sorted_sliced:
    print(c[0], end=' ')