def identificador(n1, n2):
    if n1 > n2:
        return n1, n2
    else:
        return n2, n1


def suc(n):
    return n + 1


def soma(n1, n2):
    maior, menor = identificador(n1, n2)
        
    for i in range(menor):
        maior = suc(maior)
    
    return maior


def multi(n1, n2):
    maior, menor = identificador(n1, n2)
    
    mult = 0
    
    for i in range(menor):
        mult = soma(mult, maior)
    
    return mult
    
    
def exp(n1, n2):
    expoente = 1
    
    for i in range(n2):
        expoente = multi(expoente, n1)
    
    return expoente
    