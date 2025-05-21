# 입력 받기
a, b, c = map(int, input().split())

# 리스트에 담아서 정렬
numbers = [a, b, c]
numbers.sort()

# 출력
print(numbers[0], numbers[1], numbers[2])
