n = int(input()) #반복할 횟수 입력

names = [] # 책 이름 입력 받을 리스트
for i in range(n): # 반복 횟수만큼 책 이름 입력 받기
    name = input()
    names.append(name)

# 책 이름, 횟수 저장할 딕셔너리
book_count = {}
for name in names:
    if name in book_count: #책 이름 나올 때마다 +1
        book_count[name] += 1
    else:
        book_count[name] = 1

#가장 많이 나온 횟수 구하기
max_num = max(book_count.values())

#가장 많은 횟수인 책 이름만 따로 정리
max_name = [name for name, count in book_count.items() if count == max_num]

#책 이름 정렬
max_name = sorted(max_name)
print(max_name[0]) #출력