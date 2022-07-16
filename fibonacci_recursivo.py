def fibonacci(n):  # o "n" é a posição do elemento a ser encontrado
    if n <= 1:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

# A partir de n > 50, computadores comuns já começam a demorar para retornar os valores.
 