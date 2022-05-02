from math import *


from py.calcular_raiz_quadrada_pelo_digito import *


iteracoes = 99999
for n in range(21, iteracoes):
    radicando = n**2
    
    resultado = raiz(radicando)
    
    if sqrt(radicando) != resultado:
        print("Erro !!! sqrt(%d) != %d"%(radicando, resultado))
        
        
    print( "raiz(%d) = %d | Concluido: %d%%"%(radicando,raiz(radicando), (n*100/iteracoes)) )
    
