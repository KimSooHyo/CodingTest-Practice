import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    queue = deque()
    N, M = map(int, input().split())
    documents = list(map(int, input().split()))
    
    # (index, priority) 형태로 queue 생성
    queue = deque([(i, p) for i, p in enumerate(documents)])
    cnt = 0
    
    while queue:
        element = queue.popleft()
        
        if any(element[1] < q[1] for q in queue):
            queue.append(element)
        else:
            cnt += 1
            if element[0] == M:
                print(cnt)
                break