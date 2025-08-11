import sys
input = sys.stdin.readline

N = int(input())
image = [input().split() for _ in range(N)]

def QuadTree(n, x, y):
    result = [0,0]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if image[y][x] != image[i][j]:
                half = n//2
                result = ''
                result += QuadTree(half, x, y)
                result += QuadTree(half, x+half, y)
                result += QuadTree(half, x, y+half)
                result += QuadTree(half, x+half, y+half)
                return result
    return image[y][x]
                
answer = QuadTree(N, 0, 0)
# print(answer)
print(answer.count('0'))
print(answer.count('1'))