import sys
for casos in sys.stdin:
    numero = int(casos)
    numero = int(numero ** 0.5)
    print((numero-1)*(numero)//2, (numero*(numero+1))//2)


