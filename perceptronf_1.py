entradas=[-1,7,5] #lista
pesos=[0.8,0.1,0] #lista de pesos

def soma(e,p):
    s=0
    for i in range(3):
        print(entradas[i])
        print(pesos[i])
        s+=e[i]*p[i]
        print("soma",s)
    return s 

s=soma(entradas,pesos)#chamando a função 

def stepFunction(soma):
    if (soma>=1):
        return 1 
    return 0 

r=stepFunction(s)#chamando a função e armazenando em R
print("r=",r)
