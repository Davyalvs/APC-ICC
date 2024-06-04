while True:
    try:
        N,M = map(int, input().split())
        matriz = []
        for i in range(N):
            X = list(map(int, input().split()))
            matriz.append(X)

        print(matriz)


    except EOFError:
        break