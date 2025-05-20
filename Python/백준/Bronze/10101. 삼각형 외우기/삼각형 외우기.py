# 세 각을 입력받는다
angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

angles = [angle1, angle2, angle3]

# 세 각의 합을 구한다
angle_sum = sum(angles)

if angle_sum != 180:
    print("Error")
elif angles.count(60) == 3:
    print("Equilateral")
elif angles[0] == angles[1] or angles[1] == angles[2] or angles[0] == angles[2]:
    print("Isosceles")
else:
    print("Scalene")
