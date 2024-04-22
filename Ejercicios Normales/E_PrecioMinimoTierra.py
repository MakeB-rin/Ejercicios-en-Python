t = int(input())
for i in range(0, t):
    n = int(input())
    v = []
    while(n != 0):

        v.append(n)
        n = int(input())
    v.sort()
    v.reverse()
    suma = 0
    for i in range(0, len(v)):
        suma += (2*(v[i]**(i+1)))
    if(suma <= 5000000):
        print(suma)
    else:
        print("muy caro")
