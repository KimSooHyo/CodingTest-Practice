def solution(str1, str2):
    for i in range(len(str2) - len(str1) +1):
        text = str2[i:]
        if text.startswith(str1):
            return 1
    return 0