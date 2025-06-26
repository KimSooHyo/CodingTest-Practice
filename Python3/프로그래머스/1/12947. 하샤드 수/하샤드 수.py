def solution(x):
    sum = 0
    for c in str(x):
        sum += int(c)
    if x%sum == 0:
        return True
    else:
        return False