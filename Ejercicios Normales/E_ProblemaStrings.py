# Ejercicio
# Eliminar las vocales centrales
# Entrada: tenemos que seguir correteando
# Salida:  tenmos que segir corretando
def esVocal(x):
    return x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'

# elimina la vocal
def elimina(s, v):
    ans = ""
    n = len(s)
    cnt = 0
    for i in range(n):
        if esVocal(s[i]):
            cnt += 1
        if(not esVocal(s[i])) or cnt != v//2 + 1:
            ans += s[i]
    return ans

def f(s):
    ans = ""
    n = len(s)
    i = 0
    while i < n:
        aux = ""
        vocales = 0
        while i < n and s[i] != ' ':
            aux += s[i]
            if esVocal(s[i]):
                vocales += 1
            i += 1
        if vocales%2 == 1:
            ans += elimina(aux, vocales) + " "
        else:
            ans += aux + " "
        i += 1
    return  ans

str = input()
print(f(str))
