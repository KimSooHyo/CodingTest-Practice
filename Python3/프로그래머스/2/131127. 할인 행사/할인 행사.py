def solution(want, number, discount):
    answer = 0
    for i in range(len(discount) - 9):
        check = True
        new_discount = discount[i:i+10]
        for v, w in enumerate(want):
            if new_discount.count(w) != number[v]:
                check = False
        if check == True:
            answer += 1
    return answer