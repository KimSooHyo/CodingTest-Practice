max_score = -1
max_idx = -1
for i in range(5):
    score = list(map(int, input().split()))
    if max_score < sum(score):
        max_score = sum(score)
        max_idx = i + 1
            
print(max_idx, max_score)