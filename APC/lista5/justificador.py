X = int(input())

pri = True

while X != 0:
    maior = 0
    lista = []
    
    if pri:
        pri = False
    else:
        print()

    for i in range(X):
        pal = input()
        lista.append(pal)
        if len(pal) > maior:
            maior = len(pal)

    for palavra in lista:
        if len(palavra) < maior:
            multipli = maior - len(palavra)
            print(" " * multipli+palavra)
        elif len(palavra) == maior:
            print(palavra)
    X = int(input())
    