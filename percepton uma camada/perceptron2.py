import numpy as np

entradas = np.array([0, 1])
pesos = np.array([0.5, 0.5])

def soma(e, p):
    return e.dot(p)
        
s = soma(entradas, pesos)

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

r = stepFunction(s)