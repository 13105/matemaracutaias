from py.gerar_quadrados_perfeitos import *
from py.testar_quadrado_perfeito import *
from py.gerar_quadrados_imperfeitos import *


from random import shuffle
numeros_gerados = []



gerar_quadrados_perfeitos(11,99,87, numeros_gerados)

#100
gerar_quadrados_perfeitos(100,300,30, numeros_gerados)

shuffle(numeros_gerados)
for n in numeros_gerados:
    #remove os números que são quadrados perfeitos impossiveis de detectar pelo algoritmo
    if not testar_quadrado_perfeito(n[1]):
        numeros_gerados.remove(n)
        continue

    print("%s;%s"%(n[1],n[0]))
    # numero; raiz

