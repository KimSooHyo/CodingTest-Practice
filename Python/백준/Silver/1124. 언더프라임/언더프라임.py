import sys
input = sys.stdin.readline

a, b = map(int, input().split())

n = b
primes = [0] * (n+1)
for i in range(2, n+1):
    if primes[i] == 0:
        for j in range(i, n+1, i):
            if primes[j] == 0:
                primes[j] = i
                
dp = [0] * (n+1)
for i in range(2, n+1):
    dp[i] = dp[i // primes[i]] + 1
    
def is_prime(length):
    if length < 2 :
        return False
    for i in range(2, int(length**0.5)+1):
        if length % i == 0:
            return False
    return True

cnt = 0
for i in range(a, b+1):
    if is_prime(dp[i]):
        cnt += 1
        
print(cnt)