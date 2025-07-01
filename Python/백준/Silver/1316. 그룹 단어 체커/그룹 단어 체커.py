n = int(input())
answer = 0

for _ in range(n):
    word = input()
    alpha = []
    cnt = 0
    
    for w in word:
        if not alpha:
            alpha.append(w)

        elif alpha[-1] == w or alpha.count(w) == 0:
            alpha.append(w)
            cnt += 1

    if len(word) == len(alpha):
        answer += 1

print(answer)