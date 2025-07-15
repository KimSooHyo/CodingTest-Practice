from collections import Counter
import sys
input = sys.stdin.readline

N = int(input()) #반복할 횟수 입력
num_list = [] #숫자들 저장할 리스트

#숫자들 입력 받아서 리스트에 추가
for i in range(N):
    num = int(input())
    num_list.append(num)

num_list.sort() #리스트 오름차순 정렬

print(round(sum(num_list) / N)) #산술 평균

print(num_list[N//2]) #중앙값 - N은 홀수이므로 ok

#최반값, 여러개 있는경우 두번째로 작은 값
cnt = Counter(num_list) #각 수의 빈도수 계산
max_freq = max(cnt.values()) #최빈값 계산

#최빈값이 두 개 이상인 경우를 위한 처리
max_list = [num for num, freq in cnt.items() if freq == max_freq]
max_list.sort()
if len(max_list) > 1:
    print(max_list[1])
else:
    print(max_list[0])
    
print(num_list[-1] - num_list[0]) #범위