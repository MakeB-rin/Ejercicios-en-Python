# Ejercicio
def fib(n):
    if(n <= 1):
        return n
    a = 0
    b = 1

    for i in range(2, n + 1):
        temp = b
        b = a + b
        a = temp

    return b

def potencia(x, n):
    res = 1
    base = x

    while(n > 0):
        if n % 2 == 1:
            res *= base
        base *= base
        n //= 2

    return res
def criba():
    N = 4000
    sieve = [0] * N

    pr = []
    i = 2
    while i * i < N:
        if sieve[i] == 0:
            for j in range(i * i, N, i):
                sieve[j] = 1
        i += 1

    for i in range(2, N):
        if sieve[i] == 0:
            pr.append(i)
    return pr

n = int(input())
s = 0
pr = criba()
for i in range(0, n):
    if i%2 == 0:
        s += potencia(fib(i) % 10000000, pr[i] % 10000000)
    else:
        s -= potencia(fib(i) % 10000000, pr[i] % 10000000)
print(s)
