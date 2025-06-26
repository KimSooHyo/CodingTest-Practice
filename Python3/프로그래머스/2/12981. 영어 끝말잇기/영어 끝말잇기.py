import sys

def solution(n, words):
    used = set()  # 사용된 단어 저장
    used.add(words[0])  # 첫 단어는 무조건 들어감
        
    for i in range(1, len(words)):
        prev_word = words[i - 1]
        curr_word = words[i]

        # 탈락 조건: 1. 끝말잇기 안 됨  2. 중복 단어 사용
        if curr_word in used or prev_word[-1] != curr_word[0]:
            person = (i % n) + 1
            turn = (i // n) + 1
            return [person, turn]
        
        used.add(curr_word)
        
    return [0, 0]  # 탈락자 없음