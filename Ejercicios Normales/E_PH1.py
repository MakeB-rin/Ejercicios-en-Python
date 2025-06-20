def criba(N):
    sieve = [True] * N
    sieve[0] = sieve[1] = False
    # d * d ≤ n
    for i in range(2, int(N**0.5) + 1):
        if sieve[i]: #es verdadero
            for j in range(i * i, N, i):
                sieve[j] = False
    return sieve

def contarPrimos(a, b, sieve):
    return sum(sieve[a:b+1]) #cuenta cuántos números primos hay True 1 y false 0

N = 10000000
sieve = criba(N)
casos = int(input())
for i in range(casos):
    a, b = map(int, input().split())
    print(contarPrimos(a, b, sieve))
#PH 1 2380
