# -*- coding: utf-8 -*-
"""
Created on Thu May 13 11:35:40 2021

@author: Rafael Rocha
"""

#%% Função que cria as transições do autômato que realiza o casamento
def criar_transicao(padrao, M, q, c): 
    
    # Caso o caractere analisado seja um caractere do padrão, crie uma
    # transição para o próximo estado
    if q < M and c == ord(padrao[q]):
        return q+1
  
    i=0
    
    for ns in range(q,0,-1): 
        if ord(padrao[ns-1]) == c: 
            while(i<ns-1):
                # Caso o caractere analisado não seja um caractere do padrão,
                # é criada uma transição para o estado q0
                if padrao[i] != padrao[q-ns+1+i]:
                    break
                i+=1
            # Caso o caractere analisado seja o caractere inicial do padrão,
            # uma transição é criada para o estado q1.
            # delta(q0, 'c') = q1
            if i == ns-1:
                return ns  
    return 0

#%% Função para definir a matriz de transições do autômato
def definir_transicao(padrao, M, qtd_carac):
    
    # Transições do autômato vazia (M+1 X qtd_carac).
    delta = [[0 for i in range(qtd_carac)] 
          for _ in range(M+1)]
    
    # Percorre a matriz de transições
    for q in range(M+1):
        for c in range(qtd_carac):
            # Cria as transições de cada estado através de cada caractere
            z = criar_transicao(padrao, M, q, c)
            delta[q][c] = z
            
    return delta

#%% Função casamento da palavra analisada
def casamento(T, N, M, delta):
    
    q=0
    #Percorre todo o texto
    for i in range(N): 
        # Realiza as transições do autômato para realizar o casamento
        q = delta[q][ord(T[i])]
        # Se estiver no último estado (casamento realziado), e se o próximo
        # caractere depois último caractere do padrão for espaço ou ponto, e
        # o caractere anterior ao caractere inical do padrão for espaço
        # O indice onde o padrão é encontrado é exibido
        if q == M and (T[i+1]== ' ' or T[i+1]== '.') and T[i-M]==' ': 
            print("Padrão encontrado no índice: {}". 
                   format(i-M+1))
    
    return None

#%% Parâmetro par ao casamento da palavra 'computador'

T = ("O computador é uma máquina capaz de variados tipos de tratamento "
       "automático de informações ou processamento de dados. Entende-se por "
       "computador um sistema físico que realiza algum tipo de computação. "
       "Assumiu-se que os computadores pessoais e laptops são ícones da era "
       "da informação. O primeiro computador eletromecânico foi construido "
       "por Konrad Zuse (1910-1995). Atualmente, um microcomputador é também "
       "chamado computador pessoal ou ainda computador doméstico.")

# Padrão a ser buscado
padrao = "computador"

qtd_carac = 256

M = len(padrao) 
N = len(T)


delta = definir_transicao(padrao, M, qtd_carac)

casamento(T, N, M, delta)