from statistics import *

from py.gerar_quadrados_imperfeitos import *
from py.gerar_quadrados_perfeitos import *
from py.snippets import *


def possivel_quadrado_perfeito(n):
    str_ultimos_dois_digitos = str(n)[-2:]
    n_ultimo_digito = int(str_ultimos_dois_digitos[1])
    
    if n_ultimo_digito in (2,3,7,8,0):
        if str_ultimos_dois_digitos != "00":     
            return False
        
            
    if raiz_digital(n) not in (1,4,7,9):
        return False
    
    digito_dezenas = int(str(n)[-2:][0])
    
    if n_ultimo_digito == 6:

        if not (digito_dezenas % 2):
            
            return False
    
    if n_ultimo_digito == 5:
        
        
        if digito_dezenas != 2:
            return False
    

    if not (n_ultimo_digito % 2):
        #ultimo digito é par, então os ultimos digitos obrigatoriamente devem ser divisiveis por 4
        #para o numero ser um quadrado perfeito
        ultimos_dois_digitos = (digito_dezenas*10) + n_ultimo_digito
        if ultimos_dois_digitos % 4:
            #não é divisivel por 4, então não é um quadrado perfeito.
            return False
            
    return True


#gerar_quadrados_perfeitos(20,10000000,10000, numeros_gerados)



#espaço amostral
s = []

iteracoes = 30
for i in range(0,iteracoes):
    numeros_gerados = []
    gerar_quadrados_imperfeitos(100,1000000, 10000, numeros_gerados)
    for n in numeros_gerados:
     
        linha_dados = ""
        if type(n[0]) == float:
            linha_dados += "%s;%.3f;"%(n[1],n[0])
        else:
            linha_dados += "%s;%s;"%(n[1],n[0])
            
        
        linha_dados += "%s;%s,%s"%(
            raiz_digital(n[1]),
            str(n[1])[-1:],
            possivel_quadrado_perfeito(n[1])
        )
        
        #print(linha_dados)
        
    total = len(numeros_gerados)
    possiveis = 0


    for n in numeros_gerados:
        if possivel_quadrado_perfeito(n[1]):
            possiveis+=1
            
            
            
    print("Resultado: %d/%d | %d%% dos valores não puderam ser filtrados. | %d/%d (%d%%) Não são quadrados perfeitos | Progresso total : %d%%"%(
    possiveis, 
    total,
    (possiveis * 100/total),
    (total-possiveis),
    total,
    ((total-possiveis)*100)/total,
    (i*100/iteracoes)
    ))
    s.append(possiveis * 100/total)
    
    

#print(s)    
print("Média: %s"%(mean(s)))