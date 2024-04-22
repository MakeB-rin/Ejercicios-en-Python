n = int(input())
cnt = 0
while( n != 0):
    v = [0]*n
    for i in range(0,n):
        v[i] = int(input())

    w = []
    for i in range(0, n-1):
        for j in range(i + 1, n):
            w.append(v[i] + v[j])

    q = int(input())
    cnt = cnt + 1
    print(f"Case {cnt}:")
    for i in range(0, q):
        x = int(input())
        minimo = 10000000
        ans = -1
        for j in range(0, len(w)):
            if(abs(w[j] - x) < minimo):
                minimo = abs(w[j] - x)
                ans = w[j]
        print(f"Closest sum to {x} is {ans}.")
    n = int(input())
