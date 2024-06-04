N = int(input())

Y = list(map(int, input().split()))
menor = 0
posi = 0

for i in range(N):
    if i == 0:
        menor = Y[i]
    if Y[i] < menor:
        menor = Y[i]
        posi = i

print(f'Menor valor: {menor}')
print(f'Posicao: {posi}')



