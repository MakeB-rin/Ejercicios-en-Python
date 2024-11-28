# Ejercicio
def suma(n):
    return (n*(n+1))//2

def F(n):
    return (2*(suma(n))) + suma(n-1)

t = int(input())
for casos in range(0,t):
    n = int(input())
    cnt = 0
    while(n > 1):
        cnt += 1
        a = 0
        b = 25821
        while(b - a > 1):
            med = (a + b)//2
            if(F(med) > n):
                b = med
            else:
                a = med
        n -= F(a)
    print(cnt)
