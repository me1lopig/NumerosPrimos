# código para encontrar primos con una separación específica

from sympy import isprime

def primos_gemelos(limite,separacion):
    gemelos = []
    for n in range(2, limite - 1):
        if isprime(n) and isprime(n + separacion):
            print((n, n + separacion))
    return gemelos

# Ejemplo de uso: buscar primos gemelos hasta 100
separacion = 6
limite = 10000
pares = primos_gemelos(limite,separacion)
