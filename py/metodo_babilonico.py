
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
            ---
            Não é mais rápido que o método de Newton e Joseph Raphson 
            
        Funciona a base de convergencia.
        
        
    """
    getcontext().prec = 30
    
    
    while iteracoes > 0:
        
        x = Decimal((s+x**2)/(2*x))
        
        print(x,"|", "Iteração ->",iteracoes,"\n")
        
        iteracoes-=1
        


    