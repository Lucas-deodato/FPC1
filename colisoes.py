# Algoritmo para detectar colisões em jogos eletrônicos

x0a, y0a, x1a, y1a = [int(i) for i in input().split()]
x0b, y0b, x1b, y1b = [int(i) for i in input().split()]

if x1a < x0b or x0a > x1b:
    print('0')
elif y1a < y0b or y0a > y1b:
    print('0')
else:
    print('1')
