import math
def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    
    #각 작업의 배포 가능일 계산
    days = [math.ceil((100-progresses[i])/speeds[i]) for i in range(n)]
    
    count = 0
    max_day = days[0]
    
    for i in range(n):
        if max_day >= days[i]:
            count += 1
        else:
            answer.append(count)
            count = 1
            max_day = days[i]
            
    answer.append(count)
    return answer