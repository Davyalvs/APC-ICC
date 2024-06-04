X = int(input())
dic = {}

for i in range(X):
    nome = input()
    multiplicador = float(input())

    notas = list(map(float, input().split()))
    maior = notas[0]
    menor = notas[0]

    for nota in notas:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota

    notas.remove(maior)
    notas.remove(menor)

    total = 0
    for j in notas:
        total += j

    total = total*multiplicador

    dic[nome] = total

    print(f'{nome} {dic[nome]:.2f}')

