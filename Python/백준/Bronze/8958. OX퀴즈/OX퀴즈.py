n = int(input())

def score(quiz_ans):
    cnt = 0
    total_score = 0
    for q in quiz_ans:
        if q == 'X':
            total_score += cnt
            cnt = 0
            # print('X, total = ', total_score)
            continue
        total_score += cnt
        cnt += 1
        # print("O, cnt =", cnt)
    
    total_score += cnt
    return total_score

for i in range(n):
    quiz_ans = input()
    print(score(quiz_ans))