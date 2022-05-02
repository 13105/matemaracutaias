from math import factorial
from time import sleep
from decimal import *

getcontext().prec = MAX_PREC

e = Decimal(0)
e_old = ""
for n in range(0,MAX_PREC):
    e_old = str(e)
    e = e + Decimal(1/factorial(n))
    e_str = str(e)
    
    sleep(0.1)
    

    
    
    quantidade_de_casas = 0
    for i,ch in enumerate(e_old):
        if ch != e_str[i]:
            break
        else:
            quantidade_de_casas+=1
            
    
    print(
    
    "[%d]\t%s\033[31;1m%s\033[0m"%(
    n,
    e_str[0:quantidade_de_casas],
    e_str[quantidade_de_casas:]

    )
    
    
    )
    
    if e_old == e_str:
        break
    