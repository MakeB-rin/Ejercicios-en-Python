# Ejercicio
import sys
n = sys.stdin.readline().strip()
while(n != 0):
    sum = 0
    i = 1

    f = 1
    p = len(n) - 1
    while(p >= 0):
        f = f * i
        i += 1
        sum +=(ord(n[p]) - ord('0'))*f
        p = p - 1
    print(sum)
    n = sys.stdin.readline().strip()
