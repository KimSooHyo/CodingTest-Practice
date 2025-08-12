def solution(my_string):
    answer = []
    for c in my_string:
        if ord('0') <= ord(c) <= ord('9'):
            answer.append(int(c))
    return sorted(answer)