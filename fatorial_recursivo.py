def fatorial(n):
    if n < 2:  # caso base
        return 1
    else:
        return n * fatorial(n - 1)  # passo indutivo