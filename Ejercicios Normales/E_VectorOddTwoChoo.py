def contarImpares(numero):
    lista_pares = []
    for i  in range(len(numero)-1):
        valor = numero[i:i +2]
        valor_impar = int(valor)

        if (valor_impar%2 == 1):
            lista_pares.append(valor_impar)

    return lista_pares

casos = int(input())

for _ in range(casos):
    numero = input()
    lista_numeros_impares = contarImpares(numero)
    lista_numeros_impares.sort()
    print(*lista_numeros_impares)
    #print(*[int(x) for x in valores])  # Resultado: 23 45

#Vector OddTwoChoo
