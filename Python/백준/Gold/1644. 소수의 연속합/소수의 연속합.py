import sys
input = sys.stdin.readline

def prime_num(n):
    if n < 2:
        return []
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) +1):
        if not sieve[i]:
            continue
        for j in range(i*i, n+1, i):
            sieve[j] = False
    return [i for i, isprime in enumerate(sieve) if isprime]

N = int(input())
primes = prime_num(N)

start = end = 0
nums_sum = 0
cnt = 0

while True:
    if nums_sum < N:
        if end >= len(primes):
            break
        nums_sum += primes[end]
        end += 1
    elif nums_sum > N:
        nums_sum -= primes[start]
        start += 1
    else:
        cnt += 1
        nums_sum -= primes[start]
        start += 1
        
print(cnt)