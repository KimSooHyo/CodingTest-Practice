import math

num = input()
counter = [0] * 10

#각 숫자별 개수 세기
for n in num:
    counter[int(n)] += 1
    
#6과 9를 합쳐서 다시 계산
sum = counter[6] + counter[9]
counter[6] = 0
counter[9] = 0
counter[6] = math.ceil(sum/2)

print(max(counter))