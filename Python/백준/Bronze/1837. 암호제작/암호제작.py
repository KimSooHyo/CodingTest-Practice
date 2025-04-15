def sosu(k):
    prime = [True] * k
    prime[0] = False
    prime[1] = False
    
    for i in range(2, int(k**0.5) + 1):
        if prime[i]:
            for j in range(i * i, k, i):
                prime[j] = False
                
    real_prime = [i for i, val in enumerate(prime) if val]
    
    
    return real_prime

def amho(p, k):
    primes = sosu(k)
    
    for i in primes:
        if p % i == 0:
            print("BAD", i)
            return
    print("GOOD")
    return
    
p, k = map(int, input().split())
amho(p, k)