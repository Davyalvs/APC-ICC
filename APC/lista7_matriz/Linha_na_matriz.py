L = int(input())
T = input()


matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        X = float(input())
        linha.append(X)
    matriz.append(linha)

soma = 0

for k in range(12):
    soma += matriz[L][k]

if T == "S":
    print(f'{soma:.1f}')
elif T == "M":
    print(f'{(soma/12):.1f}')