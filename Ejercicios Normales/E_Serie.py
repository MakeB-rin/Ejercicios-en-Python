# Serie
def factorial(n):
    res = 1
    for i in range(1,n+1):
        res = res*i
    return res


def fibo(n):
    a = 1
    b = 0
    c = 0
    for i in range(1,n+1):
        c = a + b
        a = b
        b = c
    return c

numero = int(input())
a = 1
cnt = 0
rango = 1
sum = 0
for i in range(1,numero+1):
    num = factorial(fibo(i))
    sum = sum + (num/a)
    cnt = cnt+1
    if(cnt == rango):
        cnt = 0
        rango = rango+1
        a = a+1

print(f"{sum:.2f}")
