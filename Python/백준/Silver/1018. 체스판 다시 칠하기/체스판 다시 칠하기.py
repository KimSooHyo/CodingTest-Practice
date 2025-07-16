n, m =map(int, input().split())
board = [input().strip() for _ in range(n)]

#체스판 기준 만들기
pattern1 = [ #W 시작
    ['W' if (i+j)%2 == 0 else 'B' for j in range(8)]
    for i in range(8)
]
pattern2 = [ #B 시작
    ['B' if (i+j)%2 == 0 else 'W' for j in range(8)]
    for i in range(8)
]

min_repaint = float('inf')

for i in range(n-7):
    for j in range(m-7):
        repaint1 = 0 #W로 시작하는 체스판 기준
        repaint2 = 0 #B로 시작하는 체스판 기준
        for x in range(8):
            for y in range(8):
                if board[i+x][j+y] != pattern1[x][y]:
                    repaint1 += 1
                if board[i+x][j+y] != pattern2[x][y]:
                    repaint2 += 1
        min_repaint = min(min_repaint, repaint1, repaint2)
                    
print(min_repaint)