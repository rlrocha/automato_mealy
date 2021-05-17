# -*- coding: utf-8 -*-
"""
Created on Sun May 16 16:58:23 2021

@author: Rafael Rocha
"""

#%% Função autômato
def verificar_cadeia(delta, qi, qf, cadeia):
    """
    
    Parameters
    ----------
    delta : 
        Transições do autômato.
    qi : 
        Estado inicial.
    qf : 
        Estados finais.
    cadeia :
        Cadeia a ser verificada.

    Returns
    -------

    q_list :
        Lista de estados percorridos.
    aceite :
        Indica se a cadeia foi aceita ou rejeitada.
    """
    
    q_list = []
    
    q = qi
    q_list.append(q)
    
    for c in cadeia:
        # Verifica se o estado possui transição por meio da letra do alfabeto 
        # analisada
        if c in delta[q]:
            # Se sim, realiza a transição para ao próximo estado
            q = delta[q][c]
            q_list.append(q)
        else:
            # Se não, a cadeia será rejeitada
            break
    
    # Verifica se o estado atual está no conjunto de estados finais
    aceite = q in qf
    
    print('Cadeia: ', cadeia.split())
    print('Estados percorridos: ',q_list)
    
    if aceite:
        print('Cadeia aceita!')
    else:
        print('Cadeia rejeitada!')
    
    return q_list, aceite

#%% Representam cada 1 seguido imediatamente de dois 0.

m1 = {'q0':{'0':'q0', '1':'q1'},
      'q1':{'0':'q2'},
      'q2':{'0':'q0'}
      }

qi = 'q0'
qf = {'q0'}
cadeia = '00110'
q_list, aceite = verificar_cadeia(m1, qi, qf, cadeia)

# cadeias = ['0', '0100', '100', '1', '1001', '010', '0001']

# for cadeia in cadeias:
#     # print('\n')
#     q_list, aceite = verificar_cadeia(m1, qi, qf, cadeia)

#%% Último simbolo seja b e o número de simbolos a seja par.

m2 = {'q0':{'a':'q1', 'b':'q2'},
      'q1':{'a':'q0', 'b':'q1'},
      'q2':{'a':'q1', 'b':'q2'}
      }

qi = 'q0'
qf = {'q2'}
cadeia = 'babab'
q_list, aceite = verificar_cadeia(m2, qi, qf, cadeia)

# cadeias = ['b', 'babab', 'baab', 'aab', 'a', 'ab', 'bab', 'aba']

# for cadeia in cadeias:
#     # print('\n')
#     q_list, aceite = verificar_cadeia(m2, qi, qf, cadeia)
