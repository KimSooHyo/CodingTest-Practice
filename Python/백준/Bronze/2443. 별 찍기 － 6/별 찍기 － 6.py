N = int(input())

for i in range(N):
    space = ' ' * i
    stars = '*' * (2 * (N - i) - 1)
    print(space + stars)
