"""
1. 임무 시작 시간, 지금 시간 입력 받기 + 0시일 경우 24시로 수정
2. 각 시간을 초로 변환
3. 임무 시작 시간 - 지금 시간
4. 초를 다시 시간, 분, 초 단위로 바꿈

---
test

임무 시작 시간 : 00:10:30
지금 시간 : 22:40:10

22:40:10
00:10:30

"""

#시간 입력
n_h, n_m, n_s = map(int, input().split(':'))
s_h, s_m, s_s = map(int, input().split(':'))

#0시일경우 24시로 수정
if s_h == '00':
    s_h = '24'
if n_h == '00':
    n_h = '24'
    
#초 단위로 바꿈    
start_time = s_h * 3600 + s_m*60 + s_s
now_time = n_h * 3600 + n_m*60 + n_s

#시간 뺀 후 다시 시 분 초로
time = (start_time - now_time) % (24 * 3600)
hour = str(time//3600)
minute = str(time//60%60)
second = str(time%60)

#출력 양식 맞춤
if len(hour) == 1:
    hour = '0'+hour
if len(minute) == 1:
    minute = '0'+minute
if len(second) == 1:
    second = '0'+second
    
print(hour+':'+minute+':'+second)