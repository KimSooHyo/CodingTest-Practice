from collections import deque

n = int(input())
skills = list(map(int, input().split()))

# 결과 덱 (초기 손에 들린 카드 상태를 재구성)
card_queue = deque()

# 역순으로 기술 적용
for i in range(n-1, -1, -1):
    card = n - i  # 현재 삽입할 카드 번호 (1부터 시작)
    
    if skills[i] == 1:
        card_queue.appendleft(card)
    elif skills[i] == 2:
        # 두 번째에 삽입 (맨 앞 다음 위치)
        card_queue.insert(1, card)
    elif skills[i] == 3:
        card_queue.append(card)

# 위에서부터 순서대로 출력
for c in card_queue:
    print(c, end=' ')
