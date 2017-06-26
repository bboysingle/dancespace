#encoding=utf8
'''
Find nth prime number
'''
from math import sqrt
def prime(maxn):
    n = 1
    while n < maxn:
        if is_prime(n):
            yield n
        n += 1
           
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for i, n in enumerate(prime(100)):
    if i == 10:
        print(n)
