import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(str, input().split())) for _ in range(N)]

mone = 0
zero = 0
one = 0

def QuadTree(n, x, y):
    for i in range(y, y + n):
        for j in range(x, x+n):
            if paper[y][x] != paper[i][j]:
                new_n = n // 3
                result = ''
                result += QuadTree(new_n, x, y)
                result += QuadTree(new_n, x + new_n, y)
                result += QuadTree(new_n, x + new_n*2, y)
                result += QuadTree(new_n, x, y + new_n)
                result += QuadTree(new_n, x + new_n, y + new_n)
                result += QuadTree(new_n, x + new_n*2, y + new_n)
                result += QuadTree(new_n, x, y + new_n*2)
                result += QuadTree(new_n, x + new_n, y + new_n*2)
                result += QuadTree(new_n, x + new_n*2, y + new_n*2)
                return result
    return paper[y][x]

        
result = QuadTree(N, 0, 0)
print(result.count('-1'))
print(result.count('0'))
print(result.count('1') - result.count('-1'))