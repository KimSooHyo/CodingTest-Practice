import sys
from collections import Counter

input = sys.stdin.readline
points = [] #상금 저장할 리스트

n = int(input()) #참여하는 사람 수 입력 받음
for i in range(n): #참여하는 사람 수만큼 반복
    #주사위 눈 입력 받아서 리스트로 저장
    nums = list(map(int, input().split()))
    count_items = Counter(nums) #가장 많이 나온 주사위 저장
    max_item = count_items.most_common(1)[0]
    
    value, cnt = max_item #주사위 값과 나온 횟수 저장
    
    #같은 눈 갯수 별로 처리
    if cnt == 3:
        points.append(10000 + (value * 1000))
    elif cnt == 2:
        points.append(1000 + (value * 100))
    else:
        points.append(max(nums) * 100)
        
#상금 리스트에서 max값 출력
print(max(points))