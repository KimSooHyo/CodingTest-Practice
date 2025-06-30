def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        s = schedules[i]

        hour = s // 100
        hour += (s % 100 + 10) // 60
        minute = (s % 100 + 10) % 60
        s = hour*100 + minute
        
        day = startday
        cnt = 0
        for j in range(7):
            
            if day == 6:
                cnt += 1
                day += 1
                continue
            elif day == 7:
                cnt += 1
                day = 1
                continue
            elif timelogs[i][j] > s:
                day += 1
                break
            elif timelogs[i][j] <= s:
                cnt += 1
                day += 1
        
        if cnt == 7:
            answer += 1
   
    return answer