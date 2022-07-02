# Algoritmo para descobrir qual peça está faltando em um quebra-cabeças

n_pecas = int(input())
conjunto_pecas = [int(i) for i in input().split()]

qc_completo = 0
qc_incompleto = 0

for i in range(1, n_pecas + 1):
    qc_completo += i

for peca in conjunto_pecas:
    qc_incompleto += peca
    
peca_faltante = qc_completo - qc_incompleto
print(peca_faltante)
