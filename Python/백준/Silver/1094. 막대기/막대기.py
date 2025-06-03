#원하는 길이 입력
num = int(input())

two = bin(num) #이진수로 변환
two = str(two) #1의 개수 세기 위해 문자열로 변환
cnt = 0

#1의 개수 세기
for t in two:
    if t == '1':
        cnt += 1
        
print(cnt)