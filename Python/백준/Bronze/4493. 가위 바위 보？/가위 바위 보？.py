def win(p1, p2):
    if p1 == p2:
        return 0  # 무승부
    elif p1 == 'R' and p2 == 'S':
        return 1  # Player 1 승
    elif p1 == 'S' and p2 == 'P':
        return 1
    elif p1 == 'P' and p2 == 'R':
        return 1
    else:
        return 2  # Player 2 승

t = int(input())

for _ in range(t):
    n = int(input())
    p1_win = 0
    p2_win = 0

    for _ in range(n):
        p1, p2 = input().split()
        result = win(p1, p2)
        if result == 1:
            p1_win += 1
        elif result == 2:
            p2_win += 1

    if p1_win > p2_win:
        print('Player 1')
    elif p1_win < p2_win:
        print('Player 2')
    else:
        print('TIE')
