from random import randint, shuffle


def gerar_cards(total):

    """
        total -> quantidade de cards (1 verdadeiro e 1 falso) gerar
        ret -> 1 card multiplo, 1 car não multiplo
    """

    multiplos_de_11 = []
    nao_multiplos_de_11 = []

    for x in range(0, total//2):
        #gera multiplos de 11
        multiplo = randint(10**4,10**6) * 11
        
        while multiplo in multiplos_de_11:
            multiplo = randint(10**3,10**4) * 11
        
        yield (True,multiplo, multiplo/11)
       
       # gera numeros que não são multiplos de 11
        n_multiplo = randint(10**5,10**7)
        while (not n_multiplo % 11) or (n_multiplo in nao_multiplos_de_11) :
            n_multiplo = randint(10**5,10**7)
           
        yield (False,n_multiplo,n_multiplo/11)
       
        


cards_gerados = [*gerar_cards(60)]
shuffle(cards_gerados)

for t in cards_gerados:
    if t[0]:
        print("%d;%s;%d"%(
            t[1],
            "Sim",
            t[2]
        ))
    else:
        print("%d;%s;%.2f"%(
            t[1],
            "Não",
            t[2]
        ))
        