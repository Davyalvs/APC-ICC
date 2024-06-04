A = 0
G = 0
D = 0


while True:
    X = int(input())

    if X == 4:
        break

    if X == 1:
        A += 1
    elif X == 2:
        G += 1
    elif X == 3:
        D += 1

print(f'MUITO OBRIGADO')
print(f'Alcool: {A}')
print(f'Gasolina: {G}')
print(f'Diesel: {D}')