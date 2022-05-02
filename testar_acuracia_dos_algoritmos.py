from math import *
from py.metodo_babilonico import *

"""
    testa precisão de 3 casas decimais do método babilônico de 1 a 100
    
"""

def gerar_quadrados_imperfeitos_precisos(quantidade):
    """ 
        Gera n quadrados imperfeitos começando do 0
        
    """
    for x in range(0,quantidade):
        
        r = sqrt(x)
        if x != int(r)**2:
            yield (x, r)
        


    
def get_quadrado_perfeito_mais_proximo(n):
    
    quadrado = 0
    for x in range(0,n):
        
        
        r = sqrt(x)
        if x < n and x == int(r)**2:
            quadrado = x
    
    return quadrado
    
quantidade = 10   
estimativas_precisas = gerar_quadrados_imperfeitos_precisos(quantidade)

for estimativa in estimativas_precisas:
    raiz_babilonica = raiz(
        estimativa[0],
        get_quadrado_perfeito_mais_proximo(estimativa[0]),
        1
    )
    
    
    print(estimativa[1])
    
    print("sqrt",estimativa[0],"=",raiz_babilonica)
    #print(raiz_babilonica, " ?= ", estimativa[1])
print(estimativas)