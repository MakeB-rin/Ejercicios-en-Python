# Ejercicio
import sys
for multiplesCasos in sys.stdin:
    temp = list(map(int,multiplesCasos.split()))
    v = []
    n = temp[0] # [1, n - 1]

    sw = 1
    for i in range(1, len(temp)):
        v.append(temp[i])
    for i in range(1, len(v)):
        if(abs(v[i] - v[i - 1]) < 1) or (abs(v[i] - v[i - 1]) >= n):
            sw = 0
    if(sw == 1):
        print("SI")
    else:
        print("NO")
