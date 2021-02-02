#Laboratorio 2Introducción a Numpy
# Instrucciones: Realice un programa en Python para resolver los siguientes problemas.

import numpy as np
M = np.array([
    [1, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1]
])

M1 = np.array([
    [1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1]
])

M2 = np.array([
    [1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1],
])

def chequeo(matriz):
    print(f'Reflexiva : {np.all(np.diagonal(matriz))}',
    f'Simetrica: {np.allclose(matriz,matriz.T)}',
    f'Transitiva: {np.allclose(matriz,np.where(matriz@matriz>1,1,matriz@matriz))}')

chequeo(M)
#Reflexiva : False Simetrica: False Transitiva: False
chequeo(M1)
#Reflexiva : True Simetrica: True Transitiva: False
chequeo(M2)
#Reflexiva : True Simetrica: True Transitiva: True
