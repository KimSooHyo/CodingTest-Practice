import datetime

# 입력 받기
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

# 오늘과 D-day 날짜 객체 생성
today = datetime.date(y1, m1, d1)
d_day = datetime.date(y2, m2, d2)

# 1000년 이상 차이나는지 직접 비교
if y2 > y1 + 1000:
    print("gg")
elif y2 == y1 + 1000 and (m2, d2) >= (m1, d1):
    print("gg")
else:
    delta = (d_day - today).days
    print(f"D-{delta}")