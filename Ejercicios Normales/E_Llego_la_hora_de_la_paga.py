while True:
    try:
        numero = int(input())
        lista = input().split()
        maximo = max([int(valor) for valor in lista])

        suma = 0
        for i in range(len(lista)):
            suma += ((int(lista[i])*100)/maximo)

        print(f"{suma:.2f}")
    except EOFError:
        break
