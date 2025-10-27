n = int(input())
a, b, c = map(int, input().split())
answer = min(n, a) + min(n, b) + min(n, c)
print(answer)