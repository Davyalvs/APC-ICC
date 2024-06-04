T = input()

matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        X = float(input())
        linha.append(X)
    matriz.append(linha)

soma = 0

for k in range(12-1):
    for l in range(k+1,12):    
        soma += matriz[k][l]



if T == "S":
    print(f'{soma:.1f}')
elif T == "M":
    print(f'{(soma/66):.1f}')