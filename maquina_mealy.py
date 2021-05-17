# -*- coding: utf-8 -*-
"""
Created on Sun May 16 18:04:46 2021

@author: Rafael Rocha
"""

#%% Função máquina de Mealy
def verificar_entrada(delta, qi, entrada):
    """
    
    Parameters
    ----------
    delta : 
        Transições da máquina de Mealy.
    qi : 
        Estado inicial.
    entrada :
        Entrada a ser verificada.

    Returns
    -------

    q_list :
        Lista de estados percorridos.
    saida :
        Saída relacionada as transições
    """
    
    entrada = entrada.split(',')
    q_list = []
    saida = []
    
    q = qi
    q_list.append(q)
    
    for e in entrada:
    
        # Verifica se a entrada é válida
        if e!='25' and e!='50' and e!='100':
            print('Entrada inválida: '+e)
            break
        
        # Obtém a saída relacionada a transição
        s = delta[q][e][1]
        saida.append(s)
        # Atualiza o estado
        q = delta[q][e][0]
        q_list.append(q)
        
    print('Entrada: ', entrada)
    print('Saídas: ', saida)
    print('Estados percorridos: ', q_list)
    
    return q_list, saida

#%% Máquina de Mealy para o fornecimento de lata de refrigerante
T_mealy = {'q0':{'25':('q1', '0'), '50':('q2', '0'), '100':('q0','1')},
           'q1':{'25':('q2', '0'), '50':('q3', '0'), '100':('q1','1')},
           'q2':{'25':('q3', '0'), '50':('q0', '1'), '100':('q2','1')},
           'q3':{'25':('q0', '1'), '50':('q1', '1'), '100':('q3','1')}
           }

qi = 'q0'
entrada = '100,25,25,25,25,100,50,50,100,100,25,50,25,50,25,25,100'
q_list, saida = verificar_entrada(T_mealy, qi, entrada)
