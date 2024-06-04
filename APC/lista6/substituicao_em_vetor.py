X = []

for _ in range(10):
    valor = int(input())
    if valor < 1:
        X.append(1)
    else:
        X.append(valor)

for indice, ans in enumerate(X):
    print(f'X[{indice}] = {ans}')