"""
M   T   W   T   F   S   S
1   2   3   4   5   6   7
8   9   10  11  12  13  14
15  16  17  18  19  20  21
22  23  24  25  26  27  28 
29  30  31  1   2   3   4
5   6   7   8   9   10  11
12  13  14  15  16  17  18
19  20  21  22  23  24  25
"""

m, d = map(int, input().split())
days = 0

day_31 = [1,3,5,7,8,10,12]
day_30 = [4,6,9,11]

days_of_week = {1 : 'MON', 2: 'TUE', 3:'WED', 4:'THU', 5:'FRI', 6:'SAT', 0:'SUN'}

for i in range(1, m):
    if m == 0 and d == 0:
        days = 1
        break
    
    if i == 2:
        days += 28
    elif i in day_31:
        days += 31
    elif i in day_30:
        days += 30
        
days += d

print(days_of_week[days%7])