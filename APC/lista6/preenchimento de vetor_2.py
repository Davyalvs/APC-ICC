N = int(input())
lista = []

contador = 0
for i in range(1000):
    lista.append(contador)
    contador += 1
    if contador == N:
        contador = 0
        
for indice, ans in enumerate(lista):
    print(f'N[{indice}] = {ans}')