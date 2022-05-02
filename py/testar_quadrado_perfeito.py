from py.snippets import raiz_digital

def testar_quadrado_perfeito(n):
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
    
