from math import *
def raiz(n):
    """
        Calcula raiz quadrada pelos digitos.
        Isso é um teste para ver se o indiano do youtube é mentiroso.

        n -> radicando
        ---------
        ret -> raiz
        
        Obs:
            Não filtrei a função para tirar a raiz de valores menores que 10, para não atrasar o programa.
    """
    if n < 10:
        return
    
    str_n = str(n)
    n_num_digitos = len(str_n)
    
    
    if n < 100:
        # 00 81 
        # 00 09
        
        
        ultimo_digito = int(str_n[1])
        parte_esquerda = 0
    
    
        
    else:
        ultimo_digito = int(str_n[-1:])
        parte_esquerda = int(str_n[:-2])
    
    
    if not n_num_digitos % 2:     
        #numero de digitos é par
        digitos_na_raiz = n_num_digitos/2
        
    else:
        #número de digitos é ímpar
        digitos_na_raiz = (n_num_digitos+1)/2
        
        
    
    
    if ultimo_digito == 1:
        possibilidades = (1,9)
        
    elif ultimo_digito == 4:
        possibilidades = (2,8)
        
    elif ultimo_digito == 9:
        possibilidades = (3,7)
        
    elif ultimo_digito == 6:
        possibilidades = (4,6)
        
    elif ultimo_digito == 5:
        possibilidades = (5,)
    
    elif ultimo_digito == 0:
        possibilidades = (0,)
        
    else:
        print("\n %d Não é um quadrado perfeito !!!"%(n))
        return False
        
    quadrado_mais_proximo = floor(sqrt(parte_esquerda))
    
    
    # X _ <- (solução_1, solução_2)
    # os digitos das casas a esquerda foram descobertos !
    
    #agora calcula o algarismo da unidade
    if quadrado_mais_proximo * (quadrado_mais_proximo+1) <= parte_esquerda:
        #o quadrado mais proximo * o seu sucessor não passou do valor da parte esquerda

        #pega o maior valor
        algarismo_da_unidade = max(possibilidades)
        
    else:
        #pega o menor valor
        algarismo_da_unidade = min(possibilidades)
    

    # raiz encontrada !
    # X X
    
    return quadrado_mais_proximo*10 + algarismo_da_unidade
