def multiplosN(n):
    divisores = set()
    for i in range(1, int(n**0.5) + 1):
        # saca del principio
        if n % i == 0:
            divisores.add(i)

        # saca del extremo final
            if i != n//i:  #1 != 10//1
                divisores.add(n // i)
    return divisores

num = int(input())
for i in range(num):
    n = int(input())
    cnt = len(multiplosN(n))
    print(f"1/{cnt}")
