from collections import deque

n, m = map(int, input().split())
targets = list(map(int, input().split()))

queue = deque(range(1, n+1))
total_ops = 0

for target in targets:
    idx = queue.index(target)
    
    # 왼쪽으로 이동하는 게 빠른 경우
    if idx <= len(queue) // 2:
        queue.rotate(-idx)  # 왼쪽으로 idx만큼
        total_ops += idx
    else:
        queue.rotate(len(queue) - idx)  # 오른쪽으로 (len - idx)만큼
        total_ops += len(queue) - idx

    queue.popleft()  # 1번 연산 (무조건 0회로 처리됨)

print(total_ops)
