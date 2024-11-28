# Ejercicio
def criba():
    N = 350
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

def mostrarMatriz(v, n, m):
    for i in range(n):
        for j in range(m):
            print(" {:d}".format(v[i][j]), end='')
        print(end = "\n")

def solve(n, m):
    global pr
    v = [[0 for i in range(m)] for j in range(n)]
    i, j = 0, -1
    aux = 1
    pos = 0
    while i < n and j < m:
        primo = pr[pos]
        pos += 1
        for k in range(primo + 1):
            j += 1
            if j == m:
                j = 0
                i += 1
        if i < n and j < m:
            v[i][j] = aux
            aux += 1
    return v

#Pricipal
n, m = map(int,input().split())
pr = criba()
ans = solve(n, m)
mostrarMatriz(ans, n, m)
