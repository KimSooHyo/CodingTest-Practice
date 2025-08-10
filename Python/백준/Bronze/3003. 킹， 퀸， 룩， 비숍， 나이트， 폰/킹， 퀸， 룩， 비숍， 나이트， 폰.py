basic = [1,1,2,2,2,8]
piece = list(map(int, input().split()))

print(*[b - p for b, p in zip(basic, piece)])