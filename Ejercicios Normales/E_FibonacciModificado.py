import sys
sys.set_int_max_str_digits(1000000)
a, b, n = map(int, input().split())

for i in range(2, n):
    c = a + b ** 2
    a, b= b, c

if n == 0:
    res = a
elif n == 1:
    res = b
else:
    res = b
print(res)
