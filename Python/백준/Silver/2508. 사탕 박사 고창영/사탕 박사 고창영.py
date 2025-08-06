import sys
input = sys.stdin.readline

t = int(input().strip())

def solution(r, c, candy):
    global cnt
    for y in range(r):
        for x in range(c):
            if candy[y][x] == 'o':
                if y > 0 and y+1 < r and candy[y-1][x] == 'v' and candy[y+1][x] == '^':

                    cnt += 1
                elif x > 0 and x+1 < c and candy[y][x-1] == '>'  and candy[y][x+1] == '<':
                    cnt += 1
    return cnt

for _ in range(t):
    a = input()
    r, c = map(int, input().split())
    candy = [list(input().strip()) for _ in range(r)]
    cnt = 0
        
    print(solution(r,c, candy))
    