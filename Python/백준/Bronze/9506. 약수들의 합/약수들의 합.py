import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break
    num_list = []
    for i in range(1, n):
        if n % i == 0:
            num_list.append(i)
            
    if sum(num_list) == n:
        print(f"{n} = "+" + ".join(map(str, num_list)))
    else:
        print(f"{n} is NOT perfect.")