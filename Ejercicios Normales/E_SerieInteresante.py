# Ejercicio
# Es una Serie
# Genera los numeros primos
def criba():
    N = 10000
    sieve = [0]*N
    
    pr = []
    i = 2
    while i*i < N:
        if sieve[i] == 0:
            for j in range(i * i, N, i):
                sieve[j] = 1
        i += 1

    for i in range(2, N):
        if sieve[i] == 0:
            pr.append(i)
    return pr

# Vector de Acumuladas
def prefix(pr):
    acc = [pr[0]]
    for i in range(1, len(pr)):
        acc.append(acc[i-1] + pr[i])
    return acc

# Solucion
def solve(n):
    global acc
    pos = 1
    value = 2
    for i in range(n):
        print("{:d}".format(value), end=" ")
        value += acc[pos]
        pos += 1


#Principal
pr = criba()
acc = prefix(pr)
n = int(input())
solve(n)
