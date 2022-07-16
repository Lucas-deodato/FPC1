# retorna o a posição do maior valor da lista
def busca_maior(L, inicio, fim):
    maior = L[inicio]
    maior_indice = inicio
    k = inicio + 1

    while k <= fim:
        if L[k] > maior:
            maior = L[k]  # armazena o maior inteiro da lista
            maior_indice = k  # armazena a posição em que está o maior valor da lista
        k += 1

    return maior_indice


while True:
    entrada = input()

    if entrada:  # se houver entrada, seguirá por aqui
            quantidade_digitos, quantidade_removidos = [int(i) for i in entrada.split()]
            lista_digitos = [int(i) for i in input()]
            
            comprimento_saldo = quantidade_digitos - quantidade_removidos  # indica a janela de busca
            inicio_janela = 0
            i = 0

            while i < comprimento_saldo:
                fim_janela = quantidade_digitos - (comprimento_saldo - i)
                maior = busca_maior(lista_digitos, inicio_janela, fim_janela)  # índice do maior valor da janela
                print(lista_digitos[maior], end='')
                inicio_janela = maior + 1
                i += 1
            print()
    else:
        break 