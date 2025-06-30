def solution(record):
    uid = {}
    
    for r in record:
        order = r.split()
        if order[0] == "Enter":
            uid[order[1]] = order[2]
            
        elif order[0] == "Change":
            uid[order[1]] = order[2]
            
    answer = []
    for r in record:
        order = r.split()
        
        if order[0] == "Enter":
            answer.append(f"{uid[order[1]]}님이 들어왔습니다.")
        elif order[0] == "Leave":
            answer.append(f"{uid[order[1]]}님이 나갔습니다.")
        
    return answer
