
def raiz_digital(n):
    """
        Calcula a raiz digital do número utilizando a formula direta.
        https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
        
    """
    if n == 0: return 0
    
    # (b-1) -> base númerica - 1 = 9
    
    return ( (n-1) % 9) + 1 
    

    
    