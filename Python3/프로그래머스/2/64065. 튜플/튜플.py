def solution(s):
    #문자열 s를 파시앟여 리스트로 변환
    s = s[2:-2].split("},{")
    s = sorted(s, key=len)
    answer = []
    
    #각 원소를 순회하면서 이전 원소와 차이나는 부분을 구함
    for element in s:
        numbers = element.split(",")
        for number in numbers:
            if int(number) not in answer:
                answer.append(int(number))
    return answer