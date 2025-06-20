def ordenar(a, b, c, d):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if a > d:
        a, d = d, a
    if b > c:
        b, c = c, b
    if b > d:
        b, d = d, b
    if c > d:
        c, d = d, c
    print(a,b,c,d)

while True:
    try:
        a,b,c,d = map(int, input().split())
        ordenar(a,b,c,d)
    except EOFError:
        break
#Ordenando 4 números
