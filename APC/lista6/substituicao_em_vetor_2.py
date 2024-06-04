X = []

valor = int(input())

for _ in range(10):
    X.append(valor)
    valor *= 2

for indice, ans in enumerate(X):
    print(f'X[{indice}] = {ans}')