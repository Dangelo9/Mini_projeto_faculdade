#versao melhorada do perceptron 1 
#usando biblioteca numpy 
#pip install numpy
import numpy as np

entradas=np.array([0,1])
pesos=np.array([0.5,0.5])

def soma(e,p):
    return e.dot(p)#dot é produto escalar

s=soma(entradas, pesos)

print(s)

def stepFunction (soma):
    if (soma>=1):
        return 1
    return 0 

r=stepFunction(s)
print(r)