def posiciones(num):
    pos = []
    lista = [int(i) for i in num]
    for i in range(len(num) - 1, -1, -1):
        if lista[i] in (0,1,2,3,5,8):
            pos.append(i)
            break
    for i in range(len(num) - 1):
        if lista[i] % 2 == 1:
            pos.append(i)
            break
    return pos

casos = int(input())
for i in range(casos):
    num = input()
    num = list(num)
    pos = posiciones(num)
    num[pos[0]], num[pos[1]] = num[pos[1]], num[pos[0]]
    res = ''.join(num)
    print(int(res))
