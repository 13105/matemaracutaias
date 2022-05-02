from random import *

"""
    Gera quadrados perfeitos aleatórios não repetidos
    a, b -> extremos do intervalo [a,b]
    quantidade -> quantidade de quadraos perfeitos que serão gerados
    -----------------------
    insere em numeros_gerados -> [(n, n^2), (n,n^2)....]
"""

def gerar_quadrados_perfeitos(a,b, quantidade, numeros_gerados):
    
    
    
    while quantidade:
        n = randint(a,b)
        tupla = (n, n**2)
        
        
        while tupla in numeros_gerados:
            
            n = randint(a,b)
            tupla = (n, n**2)
        
        numeros_gerados.append(tupla)
        quantidade-=1
    
    return
    
