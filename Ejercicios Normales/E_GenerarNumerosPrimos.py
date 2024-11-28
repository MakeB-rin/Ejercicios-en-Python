# Ejercicio
def criba(n):
    N = 100000
    sieve = [0]*N
    pr = []
    i = 2

    while i*i < N:
        if sieve[i] == 0:
            for j in range(i*i, N, i):
                sieve[j] = 1
        i += 1

    for i in range(2, N):
        if sieve[i] == 0:
           pr.append(i)
    return pr

