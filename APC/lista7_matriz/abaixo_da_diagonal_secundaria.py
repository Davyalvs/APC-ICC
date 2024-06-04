T = input()

matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        X = float(input())
        linha.append(X)
    matriz.append(linha)

soma = 0
contador = 7
for k in range(1,12):
    if k in range(1, 6):
        for l in range(12-k,12):
            soma += matriz[k][l]
    elif k in range(6, 11):
        for l in range(contador,12):
            soma += matriz[k][l]
        contador += 1
        if contador == 12:
            break

if T == "S":
    print(f'{soma:.1f}')
elif T == "M":
    print(f'{(soma/30):.1f}')

