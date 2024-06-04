N = int(input())

for _ in range(N):
    X = int(input())
    lista = []
    contador = 0
    for i in range(X):
        pal = input()
        lista.append(pal)

    for j in range(1,len(lista)):
        if lista[j] != lista[j-1]:
            print("ingles")
            contador = 1
            break
            
    
    if contador == 0:
        print(lista[0])
