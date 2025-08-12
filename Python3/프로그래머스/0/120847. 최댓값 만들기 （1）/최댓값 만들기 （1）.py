from itertools import combinations

def solution(numbers):
    answer = 0
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer = max(answer, numbers[i] * numbers[j])
    return answer