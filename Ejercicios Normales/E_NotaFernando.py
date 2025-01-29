casos = int(input())

notas_paralelo = []
promedio_notas = []
for i in range(0, casos):

    nombre = input()
    notas = input().split()
    notas_paralelo.append(sum([int(valor) for valor in notas]))
    longitud = len(notas)
    promedio_notas = [valor//longitud for valor in notas_paralelo]


promedio = sum([valor for valor in promedio_notas])
promedio_total = int(promedio)/len(promedio_notas)

maximo = max([int(valor) for valor in promedio_notas ])
minimo = min([int(valor) for valor in promedio_notas ])

print(f"Del curso 1°'D' con sus {casos} alumnos")
print(f"El promedio del curso es {int(promedio_total*10)}/100")
print(f"La nota mas baja del curso es {minimo*10}/100")
print(f"La nota mas alta del curso es {maximo*10}/100")
