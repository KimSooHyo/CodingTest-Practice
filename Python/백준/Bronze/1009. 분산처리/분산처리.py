T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    a %= 10

    if a == 0:
        print(10)
        
    #주기를 찾는 것
    else:
        cycle = []
        temp = a
        while temp not in cycle:
            cycle.append(temp)
            temp = (temp * a) % 10

        index = (b - 1) % len(cycle)
        print(cycle[index])
