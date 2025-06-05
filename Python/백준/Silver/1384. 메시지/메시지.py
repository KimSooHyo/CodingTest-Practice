# 이름, 메세지 입력 받아서 저장
def read_group(n):
    names= []
    mes = []
    
    if n == 0:
        return
    else:
        for i in range(n):
            text = input().split()
            names.append(text[0])
            mes.append(text[1:])
        return names, mes
    
# 이름, 메세지 받은 후 누가 누구에게 nasty 했는지 확인
def nasty(names, mes):
    n = len(names)
    nasty_record=[]
    
    for i in range(n):
        for j in range(n - 1):
            if mes[i][j] == 'N':
                target = (i-j-1)%n
                nasty_record.append((names[i], names[target]))    
    
    #nasty한 사람과 상대를 기록하여 리턴
    return nasty_record

#그룹 넘버를 기록해야 함(출력 조건)
groups = []
group_num = 1
while True:
    n = int(input())
    if n == 0:
        break
    else:
        #입력 받고 nasty 가려내는 함수
        names, mes = read_group(n)
        nasty_record = nasty(names, mes)
    
    #출력
    print(f"Group {group_num}")
    if not nasty_record:
        print("Nobody was nasty")
    else:
        for a, b in nasty_record:
            print(f"{b} was nasty about {a}")
    print()
    group_num += 1 #그룹 넘버 갱신