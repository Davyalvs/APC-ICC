N = int(input())
orde = {}

for _ in range(N):
    texto = input().split()
    tamanho = len(texto)

    for i in range(tamanho):
        orde[i] = texto[i]

    ordem = sorted(orde, key=lambda k: len(orde[k]), reverse=True)

    for key in ordem:
        if key == ordem[-1]:
            print(orde[key])
        else:
            print(orde[key], end=" ")
    orde = {}