while True:
    try:
        #leer el numero grande
        numero = input()
        # separar por digitos en una lista
        numero = [a for a in numero]
        # lista para almacenar los valores
        anumero = []

        for i in range(len(numero)-1, 0, -1):
            #comparar si el digito esta en esa lista
            if numero[i] in ['0','1','2','3','5','8']:
                #almacen todos los digitos que cada que encuentre un numero fib, almace el digito izq en anumero
                anumero.append(i - 1)

        #el if compara la lista numero y anumero si el 2 se encuentra numero y tambien en anumero se descarta
        # no tiene que estar (not in) para mostrar el numero

        # La posicion 0 no esta en la lista de posiciones de anumero y se considera 0 (el if por verdadero nomas pasa)
        resultado = [numero[i] for i in range(len(numero)) if i not in anumero]

        #unir toda la lista en una cadena
        resultado = ''.join(resultado)

        # volver en un entero
        print(int(resultado))

    except EOFError:
        break
    #Mi amigo el fibo
