import sys
input = sys.stdin.readline

months = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

month, day, year, time = input().split()
month = months[month]
day = int(day[:-1])
year = int(year)
hour = int(time[0:2])
minute = int(time[-2:])

# 윤년 판정
leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

total = sum(month_days) * 24 * 60
if leap:
    total += 1*24*60

present = sum(month_days[:month]) + (day-1)

if leap and month > 2:
    present += 1

present = present * 24 * 60
present += hour*60 + minute

print(present/total*100)