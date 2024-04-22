def ultimo_digito(n):
    if(n <= 4):
        f = 1
        for i in range(1, n+1):
            f = f * i
        return f%10
    else:
        return 0

t = int(input())
for i in range(0, t):
    n = int(input())
    ans = ultimo_digito(n)
    print(ans)
