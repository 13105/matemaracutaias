from random import *
from py.snippets import raiz_digital
import sys
quantidade = 10

def sim_nao(sim):
    if sim:
        return "Sim"
    
    return "Não"
 
    


def testar(quantidade): 
    for i in range(0,quantidade):

        acertos = 0
        erros = 0
        fatores = (randint(100,10**7), randint(100,10**7))
        
        
            
        # a * b = c
        produto = fatores[0] * fatores[1]
        
        
            
        
        produto_verdadeiro_digito_final = str(int(str(fatores[0])[-1:]) * int(str(fatores[1])[-1:]))[-1:]
        
        
        produto_ultimo_digito = str(produto)[-1:]
        
        
        
        fator_1_raiz_digital = raiz_digital(fatores[0])
        fator_2_raiz_digital = raiz_digital(fatores[1])
        
        # A raiz digital do produto entre as raizes digitais
        raiz_digital_do_produto_entre_as_raizes_digitais = raiz_digital(fator_1_raiz_digital * fator_2_raiz_digital)
        
        #raiz digital do resultado
        raiz_digital_do_produto = raiz_digital(produto)
        
        
        if( (raiz_digital_do_produto == raiz_digital_do_produto_entre_as_raizes_digitais) and (produto_verdadeiro_digito_final == produto_ultimo_digito)):
            acertos += 1
        else:
            erros += 1
           
        
    #retorna razão de erros para acertos
    return erros/acertos
    
s = []    
for m in range(0,100):
    s.append(testar(10000))
    
print(s, max(s))