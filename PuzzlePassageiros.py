# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 06:32:42 2024

@author: ASGUNZI
"""

import numpy as np


def simularPuzzle(N):
    #Simula puzzle dos assentos no avião.
    #Recebe N passageiros e retorna o resultado

    assentos = list(range(1,N+1))
    resultado =[]
    
    for passageiro in range(1,N+1):
        if passageiro ==1:
            #sorteia o primeiro
            sorteio = np.random.choice(assentos)
            
            assentos.remove(sorteio)
            
            #Salva no resultado
            resultado.append(sorteio)
            
        else:
            #Para os demais passageiros
            #Verifica se o seu assento está livre. Se sim, aloca
            if passageiro in assentos:
                assentos.remove(passageiro)
                #Salva no resultado
                resultado.append(passageiro)
            else:
                #Se estiver tomado, sorteia entre restantes
                sorteio = np.random.choice(assentos)
                
                assentos.remove(sorteio)
                
                #Salva no resultado
                resultado.append(sorteio)
                
    return(resultado)



#Vamos fazer 10 simulações e printar o resultado
N = 8 #Número de passageiros
for cenario in range(20):
   print(simularPuzzle(N))    