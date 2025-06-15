import math
a,b,c = map(float, input().split())
d = b**2 - 4*a*c;

if a == 0:
    print("No existe solucion")
else:
    if(d < 0):
        print("No existe solucion")
    elif (d == 0):
        r1 = -b / (2 * a)
        print("Existe una solucion")
        if abs(r1) < 1e-9:
            r1 = 0.0
        print(f"{r1:.4f}")
    else:
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        if abs(r1) < 1e-9:
            r1 = 0.0
        if abs(r2) < 1e-9:
            r2 = 0.0
        print("Existen dos soluciones")
        if(r1 < r2):
            print(f"{r1:.4f} {r2:.4f}")
        elif (r2 < r1):
            print(f"{r2:.4f} {r1:.4f}")
#Ejemplo
# x = -0.00000000001
#
# if abs(x) < 1e-9:
#     print("Es prácticamente cero")
