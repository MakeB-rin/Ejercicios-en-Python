# Ejercicios
n = int(input())
for i in range(0,n):
    a,b = map(int, input().split())
    r = (a//b)*b
    if(r != (a/b)*b):
        print("La división no es exacta. Cociente:",a//b,"Resto:",a%b)
    else:
        print("La división es exacta. Cociente:", a // b)
