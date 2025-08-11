import sys
input = sys.stdin.readline
N = int(input())
image = [input().strip() for _ in range(N)]

def QuadTree(n, x, y):
    for i in range(y, y+n):
        for j in range(x, x+n):
            if image[i][j] != image[y][x]:
                #분할 정복 코드
                half_n = n//2
                result = '('
                result += QuadTree(half_n, x, y)
                result += QuadTree(half_n, x+half_n, y)
                result += QuadTree(half_n, x, y+half_n)
                result += QuadTree(half_n, x+half_n, y+half_n)
                result += ')'
                return result
    
    return image[y][x]

print(QuadTree(N, 0, 0))