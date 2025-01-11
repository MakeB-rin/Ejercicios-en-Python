import sys
def contar_numeros_rango(lista, consulta):
    resultados = []
    for l, r in consulta:
        sub_rango = lista[l-1: r]
        numeros_unicos = set(sub_rango)
        resultados.append(len(numeros_unicos))
    return resultados


for casos in sys.stdin:
    n = int(casos)
    lista = []
    # Leer una lista mas facil y directo
    lista = list(map(int,input().split()))
    num_consultas = int(input())
    consultas = []
    for i in range(num_consultas):
        l,r = map(int, input().split())
        #Dentro de una lista tambien se puede adicionar [(1,2),(2,3)]
        consultas.append((l,r))
    #Funcion
    res = contar_numeros_rango(lista, consultas)
    for resultado in res:
        print(resultado)
