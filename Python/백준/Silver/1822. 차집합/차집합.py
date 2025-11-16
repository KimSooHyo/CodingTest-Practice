nA, nB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

result = sorted(A - B)

print(len(result))
if result:
    print(*result)