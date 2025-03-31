#입력
n, m = map(int, input().split())

#바구니 초기화
box = [0] * n

#바구니 공 넣기
for i in range(n):
    box[i] = i+1
    
for k in range(m):
    i, j = map(int, input().split())
    
    i -= 1
    j -= 1
    
    # 공 교환
    box[i], box[j] = box[j], box[i]
    
print(' '.join(map(str, box)))