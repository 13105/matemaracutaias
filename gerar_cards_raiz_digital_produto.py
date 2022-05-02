from random import *
from py.snippets import raiz_digital

quantidade = 10

def sim_nao(sim):
    if sim:
        return "Sim"
    
    return "Não"
def gerar_fatores(a,b, a_2, b_2, quantidade):

    numeros_gerados = []
    
    while quantidade:
        n = (randint(a,b), randint(a_2,b_2))
        
        
        
        
        while (n in numeros_gerados) or ( (n[1], n[0]) in numeros_gerados):           
            n = (randint(a,b), randint(a_2,b_2))
            
        
        numeros_gerados.append(n)
        
        quantidade-=1
    return numeros_gerados 
    

numeros_gerados = gerar_fatores(10**3,10**4, 10**3,10**4, 100)

baguncar = False

for fatores in numeros_gerados:
    
    # a * b = c
    produto = fatores[0] * fatores[1]
    
    if baguncar:
        produto += 10**randint(0,3) * randint(1,9)
        baguncar = False
    else:
        baguncar = True
        
    
    produto_verdadeiro_digito_final = str(int(str(fatores[0])[-1:]) * int(str(fatores[1])[-1:]))[-1:]
    
    
    produto_ultimo_digito = str(produto)[-1:]
    
    
    
    fator_1_raiz_digital = raiz_digital(fatores[0])
    fator_2_raiz_digital = raiz_digital(fatores[1])
    
    # A raiz digital do produto entre as raizes digitais
    raiz_digital_do_produto_entre_as_raizes_digitais = raiz_digital(fator_1_raiz_digital * fator_2_raiz_digital)
    
    #raiz digital do resultado
    raiz_digital_do_produto = raiz_digital(produto)
    verif = sim_nao( (raiz_digital_do_produto == raiz_digital_do_produto_entre_as_raizes_digitais) and (produto_verdadeiro_digito_final == produto_ultimo_digito))
    
    
   
    
    print("%d;%d;%d;%s;%d;%d"%(
    fatores[0],
    fatores[1],
    produto,
    verif,
    raiz_digital_do_produto_entre_as_raizes_digitais,
    raiz_digital_do_produto
    ))
    