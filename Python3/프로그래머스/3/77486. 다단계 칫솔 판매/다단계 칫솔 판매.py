def solution(enroll, referral, seller, amount):
    # parent의 딕셔너리 key는 enroll의 노드, value는 referral의 노드로 구성
    parent = dict(zip(enroll, referral))
    
    #total 딕셔너리 생성 및 초기화
    total = {name: 0 for name in enroll}
    
    #seller 리스트와 amount 리스트를 이용하여 이익 분배
    for i in range(len(seller)):
        #판매자가 판매한 총 금액 계산
        money = amount[i] * 100
        cur_name = seller[i]
        #판매자부터 차례대로 상위 노드로 이동하며 이익 분배
        while money > 0 and cur_name != '-':
            #현재 판매자가 받을 금액 계산
            total[cur_name] += money - money // 10
            cur_name = parent[cur_name]
            #현재 판매자 기준으로 분배금을 계산하기 위해 업데이트
            money //= 10
            
    return [total[name] for name in enroll]
    
    return answer