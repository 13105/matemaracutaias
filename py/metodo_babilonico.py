
from decimal import *
def raiz(s,x, iteracoes=1):
    """
        Calcula raiz quadrada utilizando o método babilônico.

        s -> a raiz que queremos descobrir
        x -> um número proximo a raiz que queremos descobrir.
        iteracoes -> a quantidade de iterações.
        
        
        Obs:
            se o número for muito distante da raiz, 
            mais iterações serão necessárias para obter uma aproximação mais precisa.
        
        Funciona a base de convergencia.
    """
    getcontext().prec = 100
    
    
    while iteracoes > 0:
        
        x = Decimal((s+x**2)/(2*x))
        
        print(x,"|", "Iteração ->",iteracoes,"\n")
        
        iteracoes-=1
        

raiz(36,9,5)
    