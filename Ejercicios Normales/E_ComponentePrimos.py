def es_primo(numero):
    if numero == 1:
        return False
    if numero == 2:
        return True

    if numero%2 == 0:
        return False
    i = 3
    while i*i <= numero:

        if numero%i == 0:
            return False
        i += 2
    return True

def lista_primos(numero):

    lista_tuplas =[]

    longitud = len(str(abs(numero)))
    valor_digito = 0

    while numero != 0:
        digito = numero//(10**(longitud-1))
        valor_digito = valor_digito + digito
        numero = numero%(10**(longitud-1))

        if(es_primo(valor_digito) and es_primo(numero) ):
            if valor_digito != 0 and numero != 0:
                lista_tuplas.append((valor_digito, numero))

        valor_digito = (valor_digito * 10)
        longitud -= 1

    return lista_tuplas

casos = int(input())
for i in range(casos):
    numero = int(input())
    res = tuple(lista_primos(numero))
    print(' '.join(str(i) for i in res))
