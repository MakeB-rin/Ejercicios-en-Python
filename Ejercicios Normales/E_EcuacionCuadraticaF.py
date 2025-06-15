a, b, c = map(int, input().split())
d = b**2 - 4*a*c;

if(d < 0):
    print("No hay solucion")
elif (d == 0):
    print("Existe una solucion")
else:
    print("Existen dos soluciones")
