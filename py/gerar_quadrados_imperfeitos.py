from random import *
from math import *

"""
    Gera quadrados IMPERFEITOS aleatórios não repetidos
    a, b -> extremos do intervalo [a,b]
    quantidade -> quantidade de quadrados imperfeitos que serão gerados
    -----------------------
    insere em numeros_gerados -> [(n, n^2), (n,n^2)....]
"""


def gerar_quadrados_imperfeitos(a,b, quantidade, numeros_gerados):
    while quantidade:
        
        n = randint(a,b)
        raiz = sqrt(n)
        
        while (int(raiz)**2 == n) or (n in numeros_gerados):
            n = randint(a,b)
            raiz = sqrt(n)
        
        numeros_gerados.append((raiz,n))
        quantidade-=1
    
    return



