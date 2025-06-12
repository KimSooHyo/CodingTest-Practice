n = int(input())

for i in range(n):
    input()
    j, b = map(int, input().split())
    j_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    
    if max(j_list) >= max(b_list):
        print('S')
    else:
        print('B')
