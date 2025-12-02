n = int(input())
mas = input()
mas = 1 if mas == 'annyong' else 0
k = int(input())

if k % 2 == mas:
    print(k)
else:
    if k + 1 <= n:
        print(k + 1)
    else:
        print(k - 1)