from sympy import isprime

def primos_gemelos(hasta):
    gemelos = []
    for n in range(2, hasta - 1):
        if isprime(n) and isprime(n + 2):
            print((n, n + 2))
    return gemelos

# Ejemplo de uso: buscar primos gemelos hasta 100
pares = primos_gemelos(100)
