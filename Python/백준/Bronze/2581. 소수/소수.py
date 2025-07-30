m = int(input())
n = int(input())

sieve = [True] * (n+1)
sieve[0] = sieve[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if sieve[i]:
        for j in range(i*i, n+1, i):
            sieve[j] = False
   
num_list = [i for i in range(m, n+1) if sieve[i]]

if num_list:
    print(sum(num_list))
    print(min(num_list))
else:
    print(-1)