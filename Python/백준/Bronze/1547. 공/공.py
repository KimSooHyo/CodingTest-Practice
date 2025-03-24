# 입력 받기
M = int(input())
cup_position = 1  # 공이 있는 컵의 초기 위치는 1

# M번의 컵 위치 변경 처리
for _ in range(M):
    X, Y = map(int, input().split())
    
    # 공이 있는 컵이 X 또는 Y 중 하나라면, 위치 변경
    if cup_position == X:
        cup_position = Y
    elif cup_position == Y:
        cup_position = X

# 결과 출력
print(cup_position)
